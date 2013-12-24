RDF Database Expectations
#########################
:date: 2010-09-02 13:45
:author: gavin
:tags: rdf
:slug: rdf-database-expectations

I use RDF databases to store 100% of O'Reilly Media's product metadata.
The catalog pages, shopping cart, electronic media distribution, product
registration process, ONIX distribution, and most internal product
reporting is based on RDF. The following are observations of what is
necessary from a RDF database in order to successfully and easily build
a similar system. As for what the clients need to be able to do...
`working on that <http://github.com/oreillymedia/pymantic>`__. The
features required are listed in descending order of priority to me.

SPARQL
------

An RDF or semantic database that does not support at least `SPARQL
1.0 <http://www.w3.org/TR/rdf-sparql-query/>`__ is not interesting.
Writing queries in Prolog, XQuery, or another DSL is not acceptable.
Getting folks to understand graphs and RDF is hard enough without also
having to teach them languages that don't work easily with graphs.

Correct
-------

When running a simple query that works fine on many other
implementations I don't expect to find INCORRECT results. Throwing
errors and saying something is unimplemented isn't great but far better
then returning results that are just WRONG.

SPARQL +
--------

SPARQL doesn't really do enough without extensions. The features I've
found to be most useful are
`LET <http://jena.sourceforge.net/ARQ/assignment.html>`__, and `GROUP
BY <http://jena.sourceforge.net/ARQ/group-by.html>`__. LET can be used
to "fake" bind parameters, create synthetic values for reports and make
complex queries much simpler. Without GROUP BY nasty post processing is
often necessary to produce summary reports from SPARQL queries. Other
helpful functions are the XPath functions, a good set of always useful
tools that I already know from years of work in XSLT and XQuery.

Named Graphs
------------

Named graphs allow me to treat the RDF database as a document store.
This rapidly reduces the complexity of loading and managing ETL
operations. The `SPARQL 1.1 Uniform HTTP Protocol for Managing RDF
Graphs <http://www.w3.org/TR/sparql11-http-rdf-update/>`__ makes me very
happy, and maps neatly on top of solutions that I'd already implemented
before I even knew the SPARQL 1.1 Working group existed. See
`Tenuki <http://github.com/oreillymedia/Tenuki>`__ for my own
implementation of graph updates over HTTP.
`ChangeSets <http://vocab.org/changeset/schema.html>`__ Talis style are
useful too, but have been more complicated to generate then I had
expected.

Concurrent
----------

I expect to be able to write updates to graphs and read from graphs at
the same time. I've encountered limitations related to Multi Reader
Single Writer locks at the graph level, dataset level, and server level.

Parses RDF/XML
--------------

Twice now I've come across products that fail to parse perfectly valid
RDF/XML. We aren't talking complex RDF/XML structures either, just
simple Literals and XMLLiterals that contain non ASCII data, or XML
mixed content.

Installable
-----------

A database server should not require me to write software in order to
use it. Simple command line clients and simple start stop scripts should
not be too much to ask.

SPARQL EXPLAIN
--------------

SPARQL query optimizers tend to be odd beasts. I have found that it's
really easy to go from a query that runs in no measurable time to one
that will, for all practical purposes, never complete. Understanding why
with EXPLAIN is hard, without EXPLAIN impossible. Profiling would of
course be better, but I’ll take what I can get.

Documented
----------

If your RDF database supports a feature but doesn't document the feature
anywhere, it doesn't support the feature. I'm should not need to read
source code to find out what SPARQL syntax and extensions the database
supports. If your products is a closed source RDF database Documentation
should really be at the top of this list as I can’t figure it out for
myself by reading the code.

License
-------

I get that databases are big money. I know Oracle owns MySQL now. It
doesn’t matter. Rails, Django, Pylons, Wicket, insert favorite SQL based
web framework here would not have existed without a good enough SQL
database like MySQL or Postgres. A semantic web framework will be
hobbled by only high cost commercial backends. A commercial database
means that we can't contribute fixes even if we want to.

Conclusion
----------

I'll deal, and do deal with a lack of most of these. But each time one
of these features is missing it's harder and harder for me to sell the
idea of using RDF and semantic databases to management. The benefits of
using RDF do in fact make up for missing tons of these features, but if
we want RDF to accepted as a model for day to day development on a par
with SQL databases these need to be addressed.
