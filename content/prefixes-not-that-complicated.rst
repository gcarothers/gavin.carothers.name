Prefixes, not that complicated.
###############################
:date: 2009-09-22 16:32
:author: gavin
:category: Uncategorized
:slug: prefixes-not-that-complicated


Summary of HTML WG Bug 7670

    | The use of prefixes that can be bound to arbitrary strings then combined with
    |  other strings to form a third set of string is IMHO too
    complicated for a
    |  technology intended for broad Web deployment (e.g. in text/html).

\ `Bug 7670 - Use of prefixes is too complicated for a Web
technology <http://www.w3.org/Bugs/Public/show_bug.cgi?id=7670>`__\ 

As stated I'm not really convinced. A few nights ago when I first saw
this I was slightly upset, my wife asked what was wrong. I ended up
bring a pad of paper to bed in order to explain. Nothing like XML/RDF
prefixes for pillow talk. I should point out that my wife knows only
some HTML and next to nothing about RDF or XML. She does have a degree
(German and History, it's important, we'll get back to this), I don't.

Anyway, as it turns out it's reasonably easy to write triples on paper
using N3 notation. After about 10 minutes my wife was having no trouble
understanding how to write statements like "The article about Michelle
Obama on The Drudge Report was issued on 2009-09-18." Then on a new page
I wrote down a changed a prefix definition! THE HORRORS! dc: now stood
for http://www.dccomics.com, "Well, that's not the same dc, so I guess I
need to use another prefix for the Dublin thingy." Not that confused
then. She pointed out that the citation method for The Chicago Manual of
Style used by a wide range of disciplines and a wide range of people is
far more complicated. It has features that would horrify the HTML WG.
Tokens whose meaning is 100% dependent on scanning backwards for the
last instance of another token (ibid), so that while copy editing it's
massively important to keep track of them when moving blocks of text
around. Shortened person and book names that are document dependent, are
the norm. Yet hundreds of thousands of people are able to use this
complex citation method. Do people screw it up? All the time. Do they
understand why and fix it? Of course.

We were able to come up with rules that make using prefixes in almost
any context simpler. Note, these are for the most part AUTHORING
guidelines, not requirements when reading:

#. Reusing the same prefix in the same document with different meanings
   is horribly confusing ("If you did that, I'd break your figures.").
   Possible to figure out, but not really desirable. Seems like a
   reasonable place for a warning.
#. Defining all the prefixes in one place makes it simpler to keep track
   of them. But understood when it would be simpler to define a new
   prefix for a section of content.
#. "Couldn't you have a simple tool that just shows you what prefixes
   are defined at any point in the document?" How such a tool has failed
   to exist in the XML world... may write this.

I really don't think prefixing as too complicated for wide adoption.
Document authors today deal with complex style guides like *The Chicago
Manual of Style*, the *Modern Language Association*, and *APA*. All of
these are at least as complicated as the notion of prefixing, some more
complicated.
