shutdown -r now
###############
:date: 2009-07-14 20:42
:author: gavin
:category: self
:slug: shutdown-r-now

Running the most recent Ubuntu builds leads to odd things happening from
time to time. This mornings little bit of joy was:

::

    -bash: shutdown: command not found

It seems that somewhere in the last ``aptitude dist-upgrade`` the
``upstart`` package had been dropped from the selected list. For those
wondering upstart provides a large number of the functions need for
init.d, and the general run level management process. There used to be a
package for systemv level compatibility where shutdown binaries lived,
that package no longer existed. Simple solution in the end, just install
upstart again.

Why do I bring this up on the blog? Well, it was time to restart the
blog again. See a few weeks ago I upgraded it too, to WordPress 2.8.1,
or rather WordPress thought it upgraded itself to 2.8.1. What really
happened is it completely broke itself to the point that it wasn't even
logging any errors. This is a nice clean fresh install of WordPress
2.8.1

I do love upgrading software on computers, always thrilling.
