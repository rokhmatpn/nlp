<!-- 
	Robb Regan Associated Press 2015
	 
-->

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"
	xmlns:msxsl="urn:schemas-microsoft-com:xslt" 
	xmlns:fn="urn:local"
                xmlns:nml="http://iptc.org/std/nar/2006-10-01/"
                xmlns:xhtml="http://www.w3.org/1999/xhtml">

	<xsl:output method="xml" omit-xml-declaration="yes"/>  	
	<xsl:preserve-space elements="*"/>

	<xsl:variable name="language">
		<xsl:text>1</xsl:text>
	</xsl:variable>
	<xsl:variable name="Category">
		<xsl:text>1</xsl:text>
	</xsl:variable>
	<xsl:variable name="AgencyCode">
		<xsl:text>2</xsl:text>
	</xsl:variable>
	<xsl:variable name="urgancy">
		<xsl:text>0</xsl:text>
	</xsl:variable>
	
	<!-- Start with root element (i.e., "<mos>") and construct XML -->
	<xsl:template match="/">
		<xsl:variable name="slug">
			<xsl:call-template name="replace-string">
				<xsl:with-param name="text" select="//itemSet/newsItem/contentMeta/altId[@type='foreignkey:SlugPrefix']"/>
				<xsl:with-param name="replace">
					<xsl:text>+</xsl:text>
				</xsl:with-param>
				<xsl:with-param name="with">
					<xsl:text>&#43;</xsl:text>
				</xsl:with-param>
			</xsl:call-template>
			<xsl:call-template name="replace-string">
				<xsl:with-param name="text" select="//newsMessage/itemSet/newsItem/contentMeta/slugline"/>
					<xsl:with-param name="replace">
					<xsl:text>+</xsl:text>
				</xsl:with-param>
				<xsl:with-param name="with">
					<xsl:text>&#43;</xsl:text>
				</xsl:with-param>
			</xsl:call-template>
		</xsl:variable>

		<!--Create new XML file -->
		<ENPSObject>
			<ENPSTitle>
				<xsl:value-of select="$slug"/> 
				<xsl:text>-</xsl:text>
				<xsl:value-of select="//itemSet/newsItem/contentMeta/altId[@type='foreignkey:StoryNumber']"/>
			</ENPSTitle>&#13;&#10;
			<ENPSText>
				<xsl:value-of select="$slug"/>&#13;&#10;<xsl:value-of select="//newsItem[contains(@guid,'-text')]/contentMeta/dateline"/>&#13;&#10;&#32;&#13;&#10;
				<xsl:apply-templates select="//newsItem[contains(@guid,'-video')]/contentSet"/>&#13;&#10;
				<xsl:apply-templates select="//newsItem[contains(@guid,'-text')]//div"/>&#13;&#10;
			</ENPSText>
			<ENPSObjectProperties>
				<Owner>
					<xsl:text>INR</xsl:text>
				</Owner>
				<Type>1</Type>
				<AnchorTime>
				  <xsl:value-of select="/newsMessage/header/sent"/>
				</AnchorTime>
				<ModTime> 
					<xsl:value-of select="/newsMessage/header/sent"/>
				</ModTime>
				<Category>
					<xsl:variable name="category" select="//newsItem[contains(@guid,'-text')]/itemMeta/service/@qcode"/>
					<xsl:choose>
						<xsl:when test="$category='apsvc:news'">
							<xsl:text>n</xsl:text>
						</xsl:when>
						<xsl:when test="$category='apsvc:ent_daily'">
							<xsl:text>e</xsl:text>
						</xsl:when>
						<xsl:when test="$category='apsvc:ent_celebrity_extra'">
							<xsl:text>c</xsl:text>
						</xsl:when>
						<xsl:when test="$category='apsvc:sntv'">
							<xsl:text>s</xsl:text>
						</xsl:when>
						<xsl:when test="$category='apsvc:sntv_arabic'">
							<xsl:text>sa</xsl:text>
						</xsl:when>
						<xsl:when test="$category='apsvc:horizons'">
							<xsl:text>h</xsl:text>
						</xsl:when>
						<xsl:when test="$category='apsvc:news_arabic'">
							<xsl:text>na</xsl:text>
		  </xsl:when>
			<xsl:when test="$category='apsvc:mideast_extra_arabic'">
			<xsl:text>meae</xsl:text> 
		 </xsl:when>
			<xsl:when test="$category='apsvc:mideast_extra'">
			<xsl:text>mee</xsl:text> 
		 </xsl:when>
			<xsl:when test="$category='apsvc:ent_now'">
			<xsl:text>en</xsl:text> 
		 </xsl:when>
			<xsl:when test="$category='apsvc:technology'">
			<xsl:text>t</xsl:text> 
		 </xsl:when>
			<xsl:when test="$category='apsvc:gns'">
			<xsl:text>g</xsl:text> 
		 </xsl:when>
			<xsl:when test="$category='apsvc:cctv'">
			<xsl:text>cctv</xsl:text> 
		 </xsl:when>
			<xsl:otherwise>
			  <xsl:text>o</xsl:text>
			</xsl:otherwise>
		  </xsl:choose>
		</Category>
		<AgencyCode>
		  <xsl:value-of select="//newsMessage/itemSet/newsItem/contentMeta/creator/@literal"/>
		</AgencyCode>
		<Priority>
		  <xsl:variable name="urgency" select="//newsMessage/itemSet/newsItem/contentMeta/urgency"/>


		  <xsl:choose>
			<xsl:when test="$urgency=0">

			  <xsl:text>f</xsl:text>
			</xsl:when>
			<xsl:when test="$urgency=1">
			  <xsl:text>b</xsl:text>
			</xsl:when>
			<xsl:when test="$urgency=2">
			  <xsl:text>u</xsl:text>
			</xsl:when>
			<xsl:when test="$urgency=3">
			  <xsl:text>r</xsl:text>
			</xsl:when>
			<xsl:when test="$urgency=4">
			  <xsl:text>r</xsl:text>
			</xsl:when>
			<xsl:when test="$urgency=5">
			  <xsl:text>r</xsl:text>
			</xsl:when>
			<xsl:when test="$urgency=6">
			  <xsl:text>r</xsl:text>
			</xsl:when>
			<xsl:when test="$urgency=7">
			  <xsl:text>d</xsl:text>
			</xsl:when>
			<xsl:when test="$urgency=8">
			  <xsl:text>x</xsl:text>
			</xsl:when>
			<xsl:when test="$urgency=9">
			  <xsl:text>x</xsl:text>
			</xsl:when>
			<xsl:otherwise>
			  <xsl:text>q</xsl:text>
			</xsl:otherwise>
		  </xsl:choose>
		</Priority>

		<StoryNumber>
		  <xsl:value-of select="//newsItem/contentMeta/altId[@type='foreignkey:StoryNumber']"/>
		</StoryNumber>
		<OutCue>
		  <xsl:value-of select="//newsItem[contains(@guid,'-text')]//div/p[last()]"/>
		</OutCue>
		<Approved></Approved>
		<GUID></GUID>
		<Version>1</Version>
		<Status>3</Status>
	  </ENPSObjectProperties>
	</ENPSObject>
	</xsl:template>


 
	<!-- Copy all the attributes and other nodes that have Body ancestor element -->
	<xsl:template match="storyBody">
    <xsl:for-each select="storyItem">
      &#13;
      <xsl:text>&lt;mos&gt;</xsl:text>
      <xsl:for-each select="*">
        <xsl:choose>
          <xsl:when test="name() = 'objPaths'">
            <xsl:text>&lt;objPaths&gt;</xsl:text>
            <xsl:for-each select="objProxyPath">
              <xsl:text>&lt;objProxyPath techDescription='</xsl:text>
              <xsl:value-of select="@techDescription"/>
              <xsl:text>'&gt;</xsl:text>
              <xsl:value-of select="text()"/>
              <xsl:text>&lt;/objProxyPath&gt;</xsl:text>
            </xsl:for-each>
            <xsl:for-each select="objProxyPath">
              <xsl:text>&lt;objPath techDescription='</xsl:text>
              <xsl:value-of select="@techDescription"/>
              <xsl:text>'&gt;</xsl:text>
              <xsl:value-of select="text()"/>
              <xsl:text>&lt;/objPath&gt;</xsl:text>
            </xsl:for-each>
            <xsl:text>&lt;/objPaths&gt;</xsl:text>
          </xsl:when>
          <xsl:otherwise>
            <xsl:call-template name="copy"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:for-each>
      <xsl:text>&lt;/mos&gt;</xsl:text>&#13;
    </xsl:for-each>
		<xsl:for-each select="p"> 
			<xsl:value-of select="."/>&#13;
		</xsl:for-each>
		&#13;&#13;
	</xsl:template>
  
  <xsl:template name="copy">
    <xsl:text>&lt;</xsl:text><xsl:value-of select="name()"/><xsl:text>&gt;</xsl:text>
    <xsl:value-of select="text()"/>
    <xsl:text>&lt;/</xsl:text><xsl:value-of select="name()"/><xsl:text>&gt;</xsl:text>
  </xsl:template>

  <xsl:template name="replace-string">
    <xsl:param name="text"/>
    <xsl:param name="replace"/>
    <xsl:param name ="with"/>
    <xsl:choose>
      <xsl:when test="contains($text,$replace)">
        <xsl:value-of select="substring-before($text,$replace)"/>
        <xsl:value-of select="$with"/>
        <xsl:call-template name="replace-string">
          <xsl:with-param name="text" select="substring-after($text,$replace)"/>
          <xsl:with-param name="replace" select="$replace"/>
          <xsl:with-param name="with" select="$with"/>
        </xsl:call-template>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="$text"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>


  <!-- Copy all the attributes and other nodes that have Body ancestor element -->
  <xsl:template match="div">
    <xsl:for-each select="p">
      <xsl:value-of select="."/>&#13;&#10;
    </xsl:for-each>
    &#13;&#10;&#32;&#13;&#10;
  </xsl:template>

  <!-- Get the last <p> tag within the <body> -->
  <xsl:template match="//htmlz">
    <xsl:apply-templates select="//body/p[last()]"/>
  </xsl:template>
  
  <xsl:template match="//contentSet" >
    &#13;
    <xsl:text>&lt;mos&gt;</xsl:text>
    <xsl:text>&lt;itemID&gt;</xsl:text>2<xsl:text>&lt;/itemID&gt;</xsl:text>
    <xsl:text>&lt;objID&gt;</xsl:text><xsl:value-of select="//itemSet/newsItem/contentMeta/altId[@type='foreignkey:StoryNumber']"/>  <xsl:text>&lt;/objID&gt;</xsl:text>
    <xsl:text>&lt;mosID&gt;</xsl:text><xsl:value-of select="//newsItem[contains(@guid,'-text')]/contentMeta/altId[@type='foreignkey:APMPMosID']"/><xsl:text>&lt;/mosID&gt;</xsl:text>
    <xsl:text>&lt;mosAbstract&gt;</xsl:text><xsl:value-of select="//newsMessage/itemSet/newsItem/contentMeta/slugline"/> : <xsl:value-of select="//newsItem/contentMeta/altId[@type='foreignkey:StoryNumber']"/><xsl:text>&lt;/mosAbstract&gt;</xsl:text>
    <xsl:text>&lt;objSlug&gt;</xsl:text><xsl:value-of select="//newsMessage/itemSet/newsItem/contentMeta/slugline"/> : <xsl:value-of select="//newsItem/contentMeta/altId[@type='foreignkey:StoryNumber']"/><xsl:text>&lt;/objSlug&gt;</xsl:text>
    <xsl:text>&lt;itemSlug&gt;</xsl:text><xsl:value-of select="//newsMessage/itemSet/newsItem/contentMeta/slugline"/> : <xsl:value-of select="//newsItem/contentMeta/altId[@type='foreignkey:StoryNumber']"/><xsl:text>&lt;/itemSlug&gt;</xsl:text>
<xsl:if test="//remoteContent/@rendition = 'rnd:highRes'">
<xsl:text>&lt;objDur&gt;</xsl:text> <xsl:value-of select="ceiling(//remoteContent[@rendition = 'rnd:highRes']/@duration * (//remoteContent/@videoframerate * 2))"/><xsl:text>&lt;/objDur&gt;</xsl:text>
<xsl:text>&lt;objTB&gt;</xsl:text> <xsl:value-of select="ceiling(//remoteContent[@rendition = 'rnd:highRes']/@videoframerate * 2)"/><xsl:text>&lt;/objTB&gt;</xsl:text>

</xsl:if>
   <xsl:if test="(//contentMeta/icon/@href) or (//remoteContent/@href)">
      <xsl:text>&lt;objPaths&gt;</xsl:text>
      <xsl:if test="(//contentMeta/icon/@href)">
        <xsl:text>&lt;objProxyPath techDescription='</xsl:text>
        <xsl:text>thumb</xsl:text>
        <xsl:text>'&gt;</xsl:text>
        <xsl:value-of select="//contentMeta/icon/@href"/>
        <xsl:text>&lt;/objProxyPath&gt;</xsl:text>
      </xsl:if>
      <xsl:for-each select="//remoteContent">
        <xsl:choose>
          <xsl:when test="@rendition = 'rnd:highRes'">
            <xsl:text>&lt;objPath techDescription='</xsl:text>
            <xsl:value-of select="@videocodec"/>
            <xsl:text>'&gt;</xsl:text>
            <xsl:value-of select="@href"/>
            <xsl:text>&lt;/objPath&gt;</xsl:text>
          </xsl:when>
          <xsl:when test="@rendition = 'rnd:preview'">
            <xsl:text>&lt;objProxyPath techDescription='</xsl:text>
            <xsl:value-of select="@videocodec"/>
            <xsl:text>'&gt;</xsl:text>
            <xsl:value-of select="@href"/>
            <xsl:text>&lt;/objProxyPath&gt;</xsl:text>
          </xsl:when>
        </xsl:choose>
      </xsl:for-each>
      <xsl:text>&lt;/objPaths&gt;</xsl:text>
    </xsl:if>
    <!--mosid-->
    <xsl:text>&lt;/mos&gt;</xsl:text>&#13;
      
  </xsl:template>
</xsl:stylesheet>

<!--
        
      [[<mos><itemID>2</itemID><itemSlug>New Row 3 Jennifer Curry</itemSlug><objID>0cccdccd-5d49-4b90-afd8-d8ae79505b39</objID><mosID>AP.MediaPort.MOS.QA</mosID><mosAbstract>++Spain Security : ap000879</mosAbstract><objPaths><objProxyPath techDescription="Preview_wmv">http://10.1.160.45/WebMedia/AP-SAMPLE-1080i50-LON-SIENNA-30s_1_6_5c9f9f71-164b-42fa-983b-c64538f16479.wmv</objProxyPath><objProxyPath techDescription="Thumbnail_jpg">http://10.1.160.45/WebMedia/AP-SAMPLE-1080i50-LON-SIENNA-30s_1_6_5c9f9f71-164b-42fa-983b-c64538f16479.jpg</objProxyPath><objPath techDescription="Preview_wmv">http://10.1.160.45/WebMedia/AP-SAMPLE-1080i50-LON-SIENNA-30s_1_6_5c9f9f71-164b-42fa-983b-c64538f16479.wmv</objPath><objPath techDescription="Thumbnail_jpg">http://10.1.160.45/WebMedia/AP-SAMPLE-1080i50-LON-SIENNA-30s_1_6_5c9f9f71-164b-42fa-983b-c64538f16479.jpg</objPath></objPaths><mosExternalMetadata></mosExternalMetadata></mos>]]
-->