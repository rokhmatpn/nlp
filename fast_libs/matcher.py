"""
Module containing methods used by 'python' type matchers.

Copyright (C) 2004-2005
Fast Search & Transfer ASA

$Id$
"""

import re

# Map from a tag or attribute specification to a compiled regular expression
# object. Used by the scopenavigator/2 method below for caching purposes.
# In a multithreaded setting, we currently assume that locking takes place
# externally. This may an assumption we have to revisit at a later stage.
_regexpmap = {}

# Precompile some regular expressions used for locating matches. Used by the
# scopenavigator/2 method below.
_tagregexp1 = re.compile("<\s*([^!/\s>]+)([^>]*)\s*>")
_tagregexp2 = re.compile("\s*([^\s\"]+)\s*=\s*\"[^\"]*\"")
_tagregexp3 = re.compile("<\s*([^!/\s>]+)(?:\s+\w+\s*=\s*\"[^\"]*\")*\s*/?\s*>")

# Define the magic begin-of-highlighting and end-of-highlighting sequences. Note that
# this must be synchronized with whatever term highlighting markup is specified in the
# fsearch.addon configuration file.
_junbohseq = chr(2)
_juneohseq = chr(3)

# Precompile some regular expressions used for locating matches. Used by the
# internal _enclosingtags/2 method below.
_junregexp1 = re.compile(_juneohseq)
_junregexp2 = re.compile("<\s*(/?[^!>\s]+)(?:\s+[^=]+\s*=\s*\"[^\"]*\")*\s*>")

# Define the tags that should be ignored when reporting back matching scopes.
# Used by the scopenavigator/2 method below. For those tags that are part of
# the standard XML "envelope", this must be synchronized with those specified
# in the fsearch.addon configuration file. For those tags that are actual
# content tags but which are not of interest to report back, this must be
# synchronized with the document processing pipeline configuration.
_ignoretags = {"matches":   1,
               "xpath":     1,
               "filter":    1,
               "error":     1,
               "match":     1,
               "sentence":  2,
               "paragraph": 2,
               "document":  2,
               "title":     2,
               "body":      2}

# Define a regular expression that can be used to strip away tags to yield
# the original surface forms. Used by the scopenavigator/2 method below.
_stripregexp = re.compile("|".join([r"(?:<[^!][^>]+>)", r"(?:<!\[CDATA\[)", r"(?:\]\]>)", _junbohseq, _juneohseq]))

# Map from a 3 character month name prefix to its number. Used by the isodate/2 method below.
_monthmap_3c = {"jan": "01",
                "ene": "01",
                "gen": "01",
                "feb": "02",
                "fev": "02",
                "mar": "03",
                "maa": "03",
                "apr": "04",
                "avr": "04",
                "abr": "04",
                "may": "05",
                "mai": "05",
                "mag": "05",
                "mei": "05",
                "jun": "06",
                "giu": "06",
                "jul": "07",
                "lug": "07",
                "aug": "08",
                "aou": "08",
                "ago": "08",
                "sep": "09",
                "set": "09",
                "oct": "10",
                "okt": "10",
                "out": "10",
                "ott": "10",
                "nov": "11",
                "dec": "12",
                "des": "12",
                "dez": "12",
                "dic": "12"}

# Map from a 4 character month name prefix to its number. Used by the isodate/2 method below.
_monthmap_4c = {u"f\u00e9v": "02",
                u"m\u00e4r": "03",
                u"juin":     "06",
                u"juil":     "07",
                u"ao\u00fb": "08",
                u"d\u00e9c": "12"}

# Precompile some regular expressions used for matching and substitution. Used by the
# nlq_quoted/2 and nlq_stopwords/2 methods below.
_nlq1regexp = re.compile(r"^\s*[\"\'].*[\"\']\s*$")
_nlq2regexp = re.compile(r"\"")
_nlq3regexp = re.compile(r"^nlquery")
_nlq4regexp = re.compile(r"[,\?\.:\(\)\s]+")

# Define a list of words that are presumably of no interest to include. Used by the
# nlq_stopwords/2 method below.
_nlqstopwords = {"about": 1, "all": 1, "also": 1, "am": 1, "and": 1, "any": 1, "an": 1, "are":1, "as": 1, "at": 1,
                 "been": 1, "be": 1, "but": 1, "by": 1,
                 "cannot": 1, "can": 1, "couldn": 1, "could": 1,
                 "didn": 1, "did":1, "doesn": 1, "does": 1, "done": 1, "do": 1,
                 "for": 1,
                 "had": 1, "hasn": 1, "has": 1, "haven": 1, "have": 1, "having": 1, "here": 1, "how": 1,
                 "if": 1, "into": 1, "in": 1, "isn": 1, "is": 1,
                 "let": 1, "ll": 1,
                 "might": 1,
                 "off": 1, "of": 1, "onto": 1, "on": 1, "or": 1, "out": 1, "over": 1,
                 "shall": 1, "shouldn": 1, "should": 1, "some": 1, "so": 1,
                 "them": 1, "then": 1, "there": 1, "these": 1, "they": 1, "the": 1, "this": 1, "those": 1, "too": 1, "to": 1,
                 "until": 1, "unto": 1, "upon": 1, "up": 1, "us": 1, "u": 1,
                 "very": 1,
                 "wasn": 1, "was": 1, "went": 1, "weren": 1, "were": 1, "we": 1, "what": 1, "when": 1, "where": 1, "whether": 1, "which": 1,
                 "whom": 1, "whose": 1, "who": 1, "why": 1, "will": 1, "with": 1, "wouldn": 1, "would": 1}

def isodate(query, context):
    """
    Normalize a variant of "April 21st, 1970" into "1970-04-21".

    This Python snippet is a companion to the date extractor. Dates are extracted
    using regular expressions, and the matching patterns are normalized by means of
    this routine. As such, this routine may have to be somewhat synchronized with
    the date extractor's main configuration file.
    """

    # Paranoia.
    query = query or ""
    context = context or ""

    # Decompose the meta data, passed as, e.g., "month2/April/day2/21/year2/1970".
    meta = context.lower().split('/')

    # Set defaults.
    year  = "XXXX"
    month = "XX"
    day   = "XX"

    # Process the meta data. Note prefix matching.
    for i in range(0, len(meta), 2):
        if meta[i].startswith("year"):
            year = meta[i + 1]
            if len(year) == 2:
                if year > "10":
                    year = "19%s" % (year)
                else:
                    year = "20%s" % (year)
        elif meta[i].startswith("month"):
            try:
                month = str(int(meta[i + 1]))
                if len(month) == 1:
                    month = "0" + month
            except:
                month = _monthmap_3c.get(meta[i + 1][0:3], month)
                if month == "XX":
                    month = _monthmap_4c.get(unicode(meta[i + 1][0:4], "utf-8"), month)
        elif meta[i].startswith("day"):
            day = meta[i + 1]
            if len(day) == 1:
                day = "0" + day

    # Swap day and month?
    if month != "XX" and day != "XX":
        if month >= "13" and day <= "13":
            month, day = day, month

    # Format the date according to the ISO 8601 standard.
    date = "%s-%s-%s" % (year, month, day)

    # Handle special cases, e.g., hardwire "XXXX-09-11" to "2001-09-11". Ideally, we'd deduce
    # this by looking at other evidence found in the same context as the incoming date.
    if date == "XXXX-09-11":
        year = "2001"
        date = "2001-09-11"

    # Return a nicely formatted ISO date as the base form, with the individual date items as meta data.
    return [(0, len(query), date, 255, 0, "/".join(["year", year, "month", month, "day", day]))]

def nlq_quoted(query, context):
    """
    Helper method for partial processing of a certain class of natural language queries.
    Please contact Aleksandra Wasiak or Juergen Oesterle for details.
    """

    query = query or ""
    context = context or ""

    # Rewrite the query to an FQL expression?
    if _nlq1regexp.search(query):
        return [(0, len(query), ''.join(['xml:document:string("', _nlq2regexp.sub('', query), '", mode="phrase")']), 255, 0, context)]
    else:
        return []

def nlq_stopwords(query, context):
    """
    Helper method for partial processing of a certain class of natural language queries.
    Please contact Aleksandra Wasiak or Juergen Oesterle for details.
    """

    query = query or ""
    context = context or ""

    # Already an FQL expression?
    if not _nlq3regexp.search(query):
        return []

    # Simple tokenization.
    terms = _nlq4regexp.split(query)
    
    if not terms:
        return []

    # Strip away stopwords.
    return  [(0, len(query), " ".join(filter(lambda x: x not in _nlqstopwords, terms)), 255, 0, context)]

def _enclosingtags(xml, all):
    """
    Internal helper function, invoked by the scopenavigator/2 method below.
    
    Given an XML snippet, locates the highlighted terms and returns a list of scopes
    that includes/encloses these. We can choose to find all enclosing scopes, or just the
    nearest one.

    The algorithm first locates the end of a highlighted term. From that offset, we then
    start locating opening or closing tags. Tags that break a certain push/pop pattern must
    necessarily include/enclose the highlighted terms.
    """

    tags = []

    # Iterate over all highlighted terms.
    for match1 in _junregexp1.finditer(xml):

        # What offsets does the match span?
        (i, j) = match1.span()
        
        stack = []

        # Find all tags that come after the highlighted term.
        for match2 in _junregexp2.finditer(xml[j:]):

            tag = match2.groups()[0]
            
            # Is it a closing tag?
            if tag[0] == '/':

                # Are we closing something we just opened?
                if stack and (tag[1:] == stack[-1]):
                    stack.pop()

                # Unexpected pattern encountered. We've found an enclosing tag!
                else:
                    tags.append(tag[1:])
                    if not all:
                        break

            # It's an opening tag. Booooring!
            else:
                stack.append(tag)
                
    return tags

def _getregexp(context):
    """
    Internal helper function, invoked by the scopenavigator/2 method below.

    Returns a regular expression object that can be used for pulling out interesting
    stuff from XML snippets.

    The returned regular expression gets cached, so that we avoid recompiling it the next
    time someone asks for it.    
    """

    # Get the precompiled regular expression, if it exists.
    recognizer = _regexpmap.get(context, None)

    # No precompiled regular expression object available?
    if not recognizer:
            
        # Create a compiled regular expression object. Handle "foo" and "foo@bar"
        # specifications.
        try:
            if not "@" in context:
                recognizer = re.compile("".join([r"<\s*", context, r"\b[^>]*>(.*?)<\s*/\s*", context, r"\s*>"]))
            else:
                (tag, attribute) = context.split("@", 1)
                recognizer = re.compile("".join([r"<\s*", tag, r"\s+[^>]*", attribute, r"\s*=\s*\"(.*?)\""]))
        except:
            return None

        # Cache it, to avoid having to recompile it later. We implicitly assume that the set of possible
        # specifications isn't overly large so that memory consumption doesn't grow indefinitely.
        _regexpmap[context] = recognizer

    # Done!
    return recognizer

def scopenavigator(query, context):
    """
    This Python snippet is a companion to shallow navigators of type 'dynamic', applied
    to XML fragments returned as matching scopes.
    """

    matches = []

    # Paranoia.
    if not query or not context:
        return matches

    # Interpret a "!" suffix as a uniqueness specification.
    unique = context.endswith("!")

    if unique:
        context = context[:-1]
        added = {}
    
    # Interpret a "?" suffix as a highlighting-constraint specification.
    constrained = context.endswith("?")

    if constrained:
        context = context[:-1]

    # This is only relevant together with a "*" specification, see below.
    constrainedall = (constrained and context.endswith("?"))

    if constrainedall:
        context = context[:-1]

    # Interpret "star" type specifications as a means for aggregating over structure instead of content.
    if (context[0] == "*"):
        star0 = True
        star1 = (context == "*")
        star2 = (context == "*@*")
    else:
        star0 = False
        star1 = False
        star2 = False

    # Apply the regular expression magic to the XML fragment. Avoid picking up XML envelope tags and other
    # ignorable stuff, if relevant. Note that position information is not needed by the client.
    # Handle "foo" and "foo@bar" context specifications, possibly constrained. Unescape some commonly escaped
    # entities (see ticket 11854 for details).
    if not star0:
        regexp = _getregexp(context)
        if regexp:
            for match in regexp.finditer(query):
                target = match.groups()[0]
                highlighted = (_junbohseq in target) or (_juneohseq in target)
                if constrained and not highlighted:
                    continue
                if ("<" in target) or highlighted:
                    target = _stripregexp.sub("", target)
                if "&" in target:
                    target = target.replace('&amp;', '&')
                    target = target.replace('&quot;', '"')
                if unique and target in added:
                    continue
                matches.append((0, 0, target, 255, 0, context))
                if unique:
                    added[target] = 1

    # Handle "*@*" context specifications.
    elif star2 and not constrained:
        for match1 in _tagregexp1.finditer(query):
            target1 = match1.groups()[0]
            if target1 in _ignoretags:
                continue
            for match2 in _tagregexp2.finditer(match1.groups()[1]):
                target2 = match2.groups()[0]
                target3 = "@".join([target1, target2])
                if unique and target3 in added:
                    continue
                matches.append((0, 0, target3, 255, 0, context))
                if unique:
                    added[target3] = 1

    # Handle "*" context specifications.
    elif star1 and not constrained:
        for match in _tagregexp3.finditer(query):
            target = match.groups()[0]
            if target in _ignoretags:
                continue
            if unique and target in added:
                continue
            matches.append((0, 0, target, 255, 0, context))
            if unique:
                added[target] = 1

    # Handle "*?" context specifications.
    elif star1 and constrained:
        for target in _enclosingtags(query, constrainedall):
            if target in _ignoretags:
                continue
            if unique and target in added:
                continue
            matches.append((0, 0, target, 255, 0, context))
            if unique:
                added[target] = 1

    # All other context specifications.
    else:
        pass

    # Let the client convert the list of all matches into content for a navigator.
    return matches
