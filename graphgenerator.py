# uncompyle6 version 3.2.5
# Python bytecode 2.3 (62011)
# Decompiled from: Python 2.7.15 (default, Jul 18 2018, 10:32:45) 
# [GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.1)]
# Embedded file name: graphgenerator.py
# Compiled at: 2012-10-12 19:09:51
"""
@author  Arnt Sch\xc3\xb8ning
@date    Creation date: 2006-01-15
@version $Id$
@file    graphgenerator.py

A module for generator a ROC graph.

Uses the Python Image Library (PIL) to create an image based on a template gif file.
"""
from common import *
from PIL import Image, ImageDraw
import getopt, os, sys, time

class ROCGraphGenerator:
    """
    Class for generator ROC graphs
    """
    __module__ = __name__

    def __init__(self):
        """
        Empty constructor
        """
        pass

    def generateROCGraphsFromFile(self, filename):
        """
        Reads and parses graph data from input file and generates ROC graphs based on these data
        
        @param filename: name of file with graph data
        @type  filename: string
        
        Format of data file is 
        
            circle (20,280) (22,282) 
            line (20,280) (57,280) 
            line (57,280) (94,280) 
            line (94,280) (280,20) 
            graphname mygraph.png  
        """
        log(L_PROGRESS, 'Trying to generate ROC graph based in data file %s' % filename)
        datafile = open(filename, 'r')
        pCircle = []
        pLine = []
        graphname = ''
        for line in datafile:
            log(L_DEBUG, 'Read line from data file: %s' % line)
            if line.startswith('circle'):
                part = line.replace('circle ', '').replace(' \n', '')
                tu = self.createNumericTuples(part)
                for t in tu:
                    pCircle.append(t)

            elif line.startswith('line'):
                part = line.replace('line ', '').replace(' \n', '')
                tu = self.createNumericTuples(part)
                for t in tu:
                    pLine.append(t)

            elif line.startswith('graphname'):
                graphname = line.replace('graphname ', '').replace('\n', '')

        datafile.close()
        log(L_DEBUG, 'Using parameters parsed from file %s %s %s' % (pCircle, pLine, graphname))
        self.generateROCpicture(pCircle, pLine, graphname)

    def createNumericTuples(self, str):
        """
        Helper method for creating a list of numeric tuples (x,y) from a input string
        
        @param str input line on the form '(x0,y0) (x1,y1)'
        @type  str string
        """
        tuList = []
        parts = str.split()
        for item in parts:
            coords = item.replace('(', '').replace(')', '')
            xy = coords.split(',')
            x = int(xy[0])
            y = int(xy[1])
            tuList.append((x, y))

        return tuList

    def generateROCpicture(self, pCircle, pLine, pFilename, pTemplateFileName):
        """
        Generates ROC graphs based on template GIF and input parameters
        
        @param pCircle: the xy coordinates for a circle
        @type  pCircle: list with tuples (x,y)
        
        @param pLine: xy coordinates for line
        @type  pLine: list with tuples (x,y)
        
        @param pFilename: name of file to save generated picture as
        @type  pFilename: string
        """
        template = Image.open(pTemplateFileName)
        draw = ImageDraw.Draw(template)
        draw.ellipse(pCircle, fill=128)
        draw.line(pLine, fill=128)
        del draw
        template.save(pFilename, 'GIF')


def usage():
    print 'Available parameters'
    print ' -f filename'
    print ' -u usage'


def parseInput():
    """
    Helper method to parse and validate command line arguments
    """
    filename = 'graphdata.txt'
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'f:u')
    except getopt.GetoptError:
        usage()
        LOG(L_ERROR, 'Error when parsing command line parameters: %s' % getopt.GetoptError)
    else:
        for o, a in opts:
            if o == '-f':
                filename = a
            elif o == '-u':
                usage()
            elif o == '--help':
                usage()
                sys.exit()
            else:
                usage()
                print 'Invalid command line option (%s) ' % o
                sys.exit()

    log(L_DEBUG, 'Command line arguments parsed, file name is %s' % filename)
    return filename


if __name__ == '__main__':
    datafilename = parseInput()
    ROCGraphGenerator().generateROCGraphsFromFile(datafilename)
    log(L_PROGRESS, 'Done drawing!')