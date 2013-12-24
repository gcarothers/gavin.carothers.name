schema.org as RDFa (Part I)
###########################
:date: 2011-06-04 08:32
:author: gavin
:category: html5, rdfa
:slug: schema-org-as-rdfa

schema.org an initiative by Google claims once again that RDFa is too
complicated. That's not really true. Here in fact are the first examples
from schema.org in RDFa. There is a bonus as well for using RDFa rather
then Microdata... `you can test that RDFa is valid and gives you what
you expect TODAY <http://www.w3.org/2007/08/pyRdfa/Shadow.html>`__.
Microdata and schema.org? No validation (STILL!), and no public parsers.

A movie
-------

The first example from Schema.org is about marking up a movie:

schema.org
    ::

        <div itemscope itemtype ="http://schema.org/Movie">
          <h1 itemprop="name"&g;Avatar</h1>
          <div itemprop="director" itemscope itemtype="http://schema.org/Person">
          Director: <span itemprop="name">James Cameron</span> (born <span itemprop="birthDate">August 16, 1954)</span>
          </div>
          <span itemprop="genre">Science fiction</span>
          <a href="../movies/avatar-theatrical-trailer.html" itemprop="trailer">Trailer</a>
        </div>

RDFa
    ::

        <div vocab="http://schema.org/" typeof="Movie">
         <h1 property="name">Avatar</h1>
         <div rel="director">Director:
           <span typeof="Person"><span property="name">James Cameron</span>
           (born <time property="birthDate" datetime="1954-08-16">August 16, 1954</time>)
           </span>
         </div>
         <span property="genre">Science fiction</span>
         <a rel="trailer" href="../movies/avatar-theatrical-trailer.html">Trailer</a>
        </div>

That wasn't very complicated. In fact compared with the example on
Schema.org, why do some attributes need fully qualified URIs/IRIs and
some don't? How does microdata know that ``director`` is refering to
schema.org's ``director`` and not some other one?

Next is Spinal Tap!
-------------------

::

    <div vocab="http://schema.org/" typeof="Event">
     <div property="name">Spinal Tap</div>
     <span property="description">One of the loudest bands ever
     reunites for an unforgettable two-day show.</span>
     Event date:
     <time property="startDate" datetime="2011-05-08T19:30">May 8, 7:30pm</time>
    </div>

Okay not even bothering with the Microdata/schema.org version. There are
a few differences but not much. Where is all this complexity that RDFa
introduces?

An offer, for a blender
-----------------------

::

    <div vocab="http://schema.org/" type="Offer">
     <span property="name">Blend-O-Matic</span>
     <span property="price">$19.95</span>
     <link rel="availability" href="http://schema.org/InStock"/>Available today!
    </div

Yeah, still not seeing why RDFa is more complicated.

Okay, that's all I feel like dealing with before breakfast. Will look a
few more later.

In the mean time, gratuitous baby pictures!

.. raw:: html

   <p>

.. raw:: html

   <embed type="application/x-shockwave-flash" width="288" height="192" src="https://picasaweb.google.com/s/c/bin/slideshow.swf" flashvars="host=picasaweb.google.com&amp;hl=en_US&amp;feat=flashalbum&amp;RGB=0x000000&amp;feed=https%3A%2F%2Fpicasaweb.google.com%2Fdata%2Ffeed%2Fapi%2Fuser%2F114808080934228018687%2Falbumid%2F5611625358674399761%3Falt%3Drss%26kind%3Dphoto%26hl%3Den_US" pluginspage="http://www.macromedia.com/go/getflashplayer">

.. raw:: html

   </embed>

.. raw:: html

   </p>

Update:
-------

By specific request, RDFa for geo tagging:

schema.org
    ::

        <div itemscope itemtype="http://schema.org/Place"
         <h1>What is the latitude and longitude of the <span itemprop="name">Empire State Building</span>?<h1>
         Answer:
         <div itemprop="geo" itemscope itemtype="http://schema.org/GeoCoordinates">
         Latitude: 40 deg 44 min 54.36 sec N
         Longitude: 73 deg 59 min 8.5 dec W
         <meta itemprop="latitude" content="40.75" />
         <meta itemprop="latitude" content="73.98" />
         </div>
        </div>

schema.org as RDFa
    ::

        <div vocab="http://schema.org/" typeof="Place"
         <h1>What is the latitude and longitude of the <span property="name">Empire State Building</span>?<h1>
         Answer:
         <div rel="geo">
         Latitude: 40 deg 44 min 54.36 sec N
         Longitude: 73 deg 59 min 8.5 dec W
         <span typeof="GeoCoordinates">
         <meta property="latitude" content="40.75" />
         <meta property="longitude" content="73.98" />
         </span>
         </div>
        </div>

RDFish RDFa
    ::

         <div prefix="schema: http://schema.org/ dc: http://purl.org/dc/terms/ pos: http://www.w3.org/2003/01/geo/wgs84_pos#" 
          typeof="schema:Place pos:SpatialThing"
         <h1>What is the latitude and longitude of the <span property="dc:title schema:name">Empire State Building</span>?<h1>
         Answer:
         Latitude: 40 deg 44 min 54.36 sec N
         Longitude: 73 deg 59 min 8.5 dec W
         <meta property="pos:latitude schema:latitude" content="40.75" />
         <meta property="pos:longitude schema:longitude" content="73.98" />
         </div>
        </div>

As with the earlier conversions, these are 5 minute jobs without really
spending much time thinking about them. But these WORK, can be validated
today and are still very simple. The RDFish version above does start to
use some RDFa features that are considered confusing. It uses 3
vocabularies rather then just one. To do this it does use the much
feared PREFIX. I've covered `my opinion of
prefixes </2009/09/22/prefixes-not-that-complicated/>`__ before. I still
stand by my statement that prefixes are simply not that complicated.
Also, the RDFish version does drop the added ``GeoCoordinates``
instance, and intermediate ``schema:geo`` property, didn't really see
why they were there. Other possible improvements include adding
datatypes to the properties in RDFa, but that's not really necessary in
this case.
