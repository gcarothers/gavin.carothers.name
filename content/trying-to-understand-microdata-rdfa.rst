Trying to understand Microdata? RDFa?
#####################################
:date: 2009-08-13 21:36
:author: gavin
:category: html5, wtf
:slug: trying-to-understand-microdata-rdfa

Been trying to follow the RDFa, microdata [STRIKEOUT:mess]\ work. This
isn't academic. I have a nice open ticket that says "Insert inline
metadata into O'Reilly Catalog pages" which is due in a large release at
the end of September.

Do I expect Google to index my page a whole lot better? Nah. (That's why
we're doing complete HTML chapters of our books, and full HTML Table of
Contents). Do I expect our internal tools to index it better? Maybe, if
I pray to the right search gods. Can I think of some some crazy shit to
do in jQuery with the few attributes I have in there? Oh yes. What
exactly is going to come of us putting micodata in our pages? No clue,
but then we didn't really know what Web 2.0 was in 2004, or this
strangeWorld Wide Web ( `Online Whole Internet
Catalog <http://www.archive.org/details/wholeinternet00krolmiss>`__, in
which we uh, printed the internet) thing was in 1992.

Lets get started. I know what metadata I need to express. Here is a
short version of it expressed in Turtle. There are a number of other
fields, but this will give you the gist.

::

    @prefix dc: <http://purl.org/dc/terms/> .
    @prefix frbr: <http://purl.org/vocab/frbr/core#> .

    <http://purl.oreilly.com/works/45U8QJGZSQKDH8N> a frbr:Work ;
         dc:creator "Wil Wheaton"@en ;
         dc:title "Just a Geek"@en ;
         frbr:realization <http://purl.oreilly.com/products/9780596007683.BOOK>,
             <http://purl.oreilly.com/products/9780596802189.EBOOK> . 

    <http://purl.oreilly.com/products/9780596007683.BOOK> a frbr:Expression ;
         dc:type <http://purl.oreilly.com/product-types/BOOK> . 

    <http://purl.oreilly.com/products/9780596802189.EBOOK> a frbr:Expression ;
         dc:type <http://purl.oreilly.com/product-types/EBOOK> .

This sample uses two vocabularies that exist in the wild. `Dublin
Core <http://dublincore.org/documents/dcmi-terms/>`__, which is a very
mature standard developed by a reasonably heavy weight process with many
serializations, and uses. FRBR too is a standard developed by a rather
austere body the `International Federation of Library Associations and
Institutions <http://en.wikipedia.org/wiki/International_Federation_of_Library_Associations_and_Institutions>`__
the `RDF realization <http://vocab.org/frbr/core>`__ of it however isn't
from them but rather a few guys who needed to represent it. Reasonably
smart few guys, but no giant standards body here.

Took about 15 minutes to whip up a `simple RDFa based
representation <http://gavin.carothers.name/microdata/geek-rdfa.html>`__.
Now, I know RDF reasonably well, XML very well, and have decent HTML
skills. So I admit my experience is not going to be the norm, but it
didn't feel a whole lot harder then the first time I was trying to use
hCard. I screwed up a few times, mixing up where to use rel= vs.
property=. I also forgot that I can't just stick a <UL> in another <UL>,
need the picky <LI>, also left off at least one close tag. Made all
those mistakes in just 32 lines of HTML. But a few quick iterations with
validation and it was all green check boxes. I screwed up my late night
hand written HTML at about the same rate I screwed up RDFa attributes. I
had read the RDFa primer two months ago, but didn't remember much other
then there were some attributes and they went on some tags. Didn't use
the primer, just looked at the example content from
`RDFa4Google <http://www.ebusiness-unibw.org/wiki/Rdfa4google>`__. Used
`Elias Torres RDFa parser <http://torrez.us/rdfa/>`__ to test my results
and `validator.w3.org <http://validator.w3.org/>`__ for my HTML.

Felt reasonably happy with my RDFa result. Worked as expected. Microdata
time!

Okay, got my Microdata spec. Finding a validator or parser however did
not go well. 5 minutes in Google and Bing, turned up the expected HTML5
validator.nu but nothing in the way of a microdata validator or parser.
I'll be honest I was very tempted to stop here. Given the mistakes I
made with RDFa, I'm very skeptical of my ability to write Microdata
without the help of a parser. But I imagine there is one, and once I
post this someone will tweet about it 5 minutes later.

Huh, okay, I have my outer item for the Work:

::

    <div id="http://purl.oreilly.com/works/45U8QJGZSQKDH8N" 
                    item="http://purl.org/vocab/frbr/core#Work">
        <ul>
            <li><label>Title:</label>
              <span itemprop="http://purl.org/dc/terms/title">
                Just a Geek</span></li>
            <li><label>By</label>
              <span itemprop="http://purl.org/dc/terms/creator">
                Wil Wheaton</span></li>

That wasn't very hard at all. I'm completely lost at how to relate that
work to the two expressions however. It looks like I'm limited to my
microdata being in an <a> tag link to the expressions. And I really
don't understand the idea behind:

    The value is the element's textContent.

Does this mean I can't use any data that isn't displayed directly on the
page? If the data would be better expressed in a machine readable form?
In my case product type \ http://purl.oreilly.com/product-types/EBOOK
really isn't very human friendly. Ideas on how to express the same
metadata or equivalent in microdata are very welcome. `This is the best
I could
do <http://gavin.carothers.name/microdata/geek-microdata.html>`__.

I was expecting more tooling and examples from Microdata given it's
inclusion in HTML5. I was very surprised by the lack of tooling and
almost complete lack real world examples.
