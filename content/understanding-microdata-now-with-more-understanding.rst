Understanding Microdata, now with more understanding
####################################################
:date: 2009-08-18 09:44
:author: gavin
:tags: html5
:slug: understanding-microdata-now-with-more-understanding

Okay, I'm giving this whole HTML5 microdata a shot for real. 4475 HTML
pages of it in fact.

After reading what `Hixie <http://ln.hixie.ch/>`__ wrote, tried creating
a `new
sample <http://gavin.carothers.name/microdata/geek-microdata-better.html>`__.
Didn't feel any stranger then the markup for RDFa. From a typing
perspective, it is annoying to have to type the whole URI, from a
reading perspective it's much clearer what's going on, at least to me. I
also won't be typing these every time, template systems are neat like
that. Now as far as I can tell the XHTMLy solution to this using XML
entities is not supported in HTML5.

Should have known better then to jump right from the sample into doing
template markup. Having spent the morning making sure that I was
producing valid HTML5, the addition of microdata caused errors at
Validator.nu. It seems the method of using ``<link>`` elements is not
currently supported by the validator. In fact even our sample `fails to
validate <http://validator.nu/?doc=http%3A%2F%2Fgavin.carothers.name%2Fmicrodata%2Fgeek-microdata-better.html&showsource=yes>`__.
Ugh.

Philip's parser works nicely for testing to see if what I have is
working, given that I can't use the validator.

At this point I have markup for the relationships of Manifestations of
an edition (Expression). Adding the markup for the publication dates was
much more unpleasant. It seems that I have to repeat the whole:

::

    <some_tag
         itemprop="http://vocab.org/frbr/core#embodiment"
         item="http://purl.org/vocab/frbr/core#Manifestation">
         <link itemprop="about" href="${product.subject}">

every time I need to talk about ${product.subject}. And the microdata
parser happily adds the relationship all over again.

::

      <http://vocab.org/frbr/core#embodiment> <urn:x-domain:oreilly.com:product:9780596007683.BOOK> ;
      <http://vocab.org/frbr/core#embodiment> <urn:x-domain:oreilly.com:product:9780596806316.BOOK> ;
      <http://vocab.org/frbr/core#embodiment> <urn:x-domain:oreilly.com:product:9780596802189.EBOOK> ;
      <http://vocab.org/frbr/core#embodiment> <urn:x-domain:oreilly.com:product:9780596802028.SAF> ;
      <http://vocab.org/frbr/core#embodiment> <urn:x-domain:oreilly.com:product:9780596007683.BOOK> ;
      <http://vocab.org/frbr/core#embodiment> <urn:x-domain:oreilly.com:product:9780596806316.BOOK> ;
      <http://vocab.org/frbr/core#embodiment> <urn:x-domain:oreilly.com:product:9780596802189.EBOOK> .
        .

There is a great deal of markup smell coming `from this page
now <http://gavin.carothers.name/microdata/geek-real-microdata.html>`__.
I think from here I'm going to try this as XHTML (5?) and go back to
RDFa and see how that goes.

Will send this and earlier post to WhatWG mailing list as soon as my
subscription to the WhatWG mailing list is approved.
