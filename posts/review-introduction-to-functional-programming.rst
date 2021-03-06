.. title: Review: Introduction to Functional Programming
.. slug: review-introduction-to-functional-programming
.. date: 2015-01-03 05:47:51 UTC
.. tags: programming
.. link: 
.. description: 
.. type: text

Recently I completed Delft University's fall 2014 offering of `Introduction to Functional Programming (FP101x) <https://www.edx.org/course/introduction-functional-programming-delftx-fp101x>`_ on edX. I've been interested in functional programming for a while (caught the bug when I learned about Python list comprehensions), so I was really excited for this class. It turned out to be one of the better MOOCs I've taken, and definitely the most challenging.

My takeaways from the class:

Functional programming is cool
==============================

Erik Meijer, the professor, is funny and brilliant, and I came away from many of his lectures thinking, wow, that was fascinating. I've read before that learning how to program in a functional style is like learning how to code all over again, which I found to be true. This class opened my mind to a totally different way of reasoning about the structure and composition of programs.

Beginners, beware
=================

The prerequisite for FP101x is at least one year of experience programming in an imperative language. I've been working with JavaScript since early 2013, and I learned basic Python and C before that, so you'd think I would be fine. NOPE. Both the homework (multiple choice) and labs (programming assignments) started off simple but got mind-numbingly difficult toward the end. The last two labs in particular really stumped me -- we had to implement Poor Man's Concurrency and rose trees, two subjects that weren't even hinted at in the lectures. And don't even get me started on monads.

I got the sense that Prof. Meijer doesn't typically teach beginners. Based on the assignments and his forum posts, he seemed to have really high expectations of what a MOOC student would be able to accomplish with little guidance and limited time. For me, a total novice, the second half of the class was a struggle. Fortunately, there were plenty of kind, generous folks who took the time to help out their classmates in the forums.

To anyone who's considering taking FP101x: learn a bit about `category theory <http://en.wikipedia.org/wiki/Category_theory>`_ first. Also, `basic Haskell <http://learnyouahaskell.com/>`_ would be good. The class is language-agnostic, but Prof. Meijer used Haskell in all the lectures and homework assignments. From my travels around the discussion forums I'd wager that most of us ended up solving the labs in Haskell, too, although the instructions were provided in multiple languages (Scala, F#, Groovy, Frege, Ruby). It would have been much easier for me to digest the concepts in this class if I hadn't had to learn an entirely new language as well.

But, speaking of Haskell...
===========================

Seriously, what a gorgeous language.

I don't understand it. That is, I understand enough of it to know I don't understand it at all. Regardless, I can still appreciate it on a superficial level.

Say you have a list, and you want to apply one function to the members of the list in odd positions, and another function to the members of the list in even positions. Here's a quick JavaScript implementation:

::

  function oddEvenMap(list, oddFunc, evenFunc) {
    for (var i = 0; i < list.length; i++) {
      if (i % 2 === 0) {
	evenFunc(list[i]);
      } else {
	oddFunc(list[i]);
      }
    }
  }
  
  
And here it is in Haskell:

::

  oddEvenMap :: (a -> b) -> (a -> b) -> [a] -> [b]
  oddEvenMap f g [] = []
  oddEvenMap f g (x : xs) = f x : oddEvenMap g f xs

No variable assignments. No for loops. Haskell is stunningly beautiful and concise. (I realize the comparison to JavaScript isn't fair, but that's the language I know best.)

Lastly, edX is a great MOOC platform
====================================

In 2014, Coursera was my MOOC platform of choice, as I'd finished three classes through it at the end of 2013 (`Computing for Data Analysis <https://www.coursera.org/course/compdata>`_, `Data Analysis <https://www.coursera.org/course/dataanalysis>`_, and `Machine Learning <https://www.coursera.org/course/ml>`_).

Now edX has taken its place, primarily for usability reasons. Coursera's interface is passable, with many Bootstrappy elements; the videos seem to go on forever. edX's interface is thoughtful and intuitive. Two of my favorite aspects: the video player, which has speed controls and highlighted subtitles that scroll in unison with the instructor's speech, and the homework submission system, which checks each answer individually.

I will definitely be returning to edX for more classes later this year.
