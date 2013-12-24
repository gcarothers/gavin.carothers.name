time vs data
############
:date: 2011-10-30 13:30
:author: gavin
:tags: html5
:slug: time-vs-data

There is a `bug in HTML5 to remove time and replace it with
data <http://www.w3.org/Bugs/Public/show_bug.cgi?id=13240>`__.

I think in general that ``<data>`` isn't a bad idea. I agree that only
being able to talk about ``<time>`` was a bit odd, and that many other
values have the same effective use case. As mentioned `by Ian
Hixen <http://www.w3.org/Bugs/Public/show_bug.cgi?id=13240#c14>`__:

-  dimensionless numbers (2.3)
-  numbers with units (5kg)
-  enumerated values, like months (February) or days of the week
   (Monday)
-  durations

However, I don't think that data as it stands right now is done. As this
example of the old ``<time>`` and new ``<data>`` shows there is a fairly
heavy semantics loss from the change.

::

    Published <time pubdate datetime="2009-09-15T14:54-07:00">on 2009/09/15 at 2:54pm</time> 

Assigned data to RDF via magic human transformation step simply to talk
about what data is there. Displayed in
`Turtle <http://www.w3.org/TR/turtle/>`__.

::

     @prefix magic: <http://gavin.carothers.name/vocabs/magic#> . 
    <> magic:pubdate "2009-09-15T14:54-07:00"^^xsd:dateTime . 

The HTML contains a reasonable amount of data. We know that the contents
of datatime is an ISO datatime, we know that the relationship between
that date time and the page is it's publication date.

::

    Published <data value="2009-09-15T14:54-07:00">on 2009/09/15 at 2:54pm</data> 

Again magic human transformation to Turtle.

::

    @prefix magic: <http://gavin.carothers.name/vocabs/magic#> . 
    [] magic:unknown "2009-09-15T14:54-07:00" . 

This time around don't know much at all. We know that
"2009-09-15T14:54-07:00" may some how be related to the current page. We
don't know how the string is formated, nor how the string is related to
the page if it is at all.

As currently proposed ``<data>`` sure looks like a step backwards, but
maybe it can be a step forward.

Just some invalid markup:

::

    <data type="dateTime" value="2009-09-15T14:54-07:00" property="pubdate"> 

Just some RDFa:

::

    <data datatype="xsd:dateTime" content="2009-09-15T14:54-07:00" property="magic:pubdate"> 

Just some microdata plus some datatype:

::

    <data type="dateTime" value="2009-09-15T14:54-07:00" itemprop="pubdate"> 

Adding a generic data element without data typing doesn't seem like a
good idea. With datatyping I can see it working better then creating an
element for every kind of data.
