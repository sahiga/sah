.. link: 
.. description: 
.. tags: linux, git, version control
.. date: 2013/05/05 21:05:00
.. title: GitHub for Linux Mint
.. slug: github-for-linux-mint

Version control terrifies me.

But you know what else terrifies me? Losing files. I've lost enough of them and endured enough filename headaches (story-1.doc, story-2.doc, story-final, story-new.doc, story-newEST.doc, etc.) in my lifetime to realize that **version control is extremely important**, and I need to develop better version control habits.

So, I added the files for this site to `my GitHub account <https://github.com/sahiga/sah>`_. The following guide details the steps I took, minus the legion of errors I made. I've named it "GitHub for `Linux Mint <http://www.linuxmint.com>`_," in honor of my operating system and the fact that GitHub offers `GitHub for Mac <http://mac.github.com>`_ and `GitHub for Windows <http://windows.github.com>`_, but no GitHub for GNU/Linux (even though, hey, some of us GNU/Linux users could use a little point-and-click help over here).

	Note: Afterward, I realized I could have had a `much easier time <https://help.github.com/articles/fetching-a-remote>`_ cloning the repository. This command is identical to the "Clone in Windows" and "Clone in Mac" buttons in the corresponding GitHub GUI applications::

		git clone <URL>


Connect your computer to GitHub
===============================

First, you need a secure method of connecting your computer to GitHub. You can do this through SSH (generate a new public/private SSH key pair and add it to your GitHub account) or through HTTPS (configure the Git credential helper).

- `Instructions for using HTTPS with GitHub <https://help.github.com/articles/set-up-git>`_
- `Instructions for using SSH with GitHub <https://help.github.com/articles/generating-ssh-keys>`_

Prepare the branches
====================

`Create a new repository on GitHub <https://github.com/new>`_. This is the **remote branch**.

Fire up your command line. Move to the directory containing your version control files (if you're not there already), e.g., ``cd sah``.

Initialize a Git repository in this directory. This is the **local branch**.

::

	git init

Check the status of your new repository.

::

	git status

(or ``git st`` if you've set up `aliases <http://git-scm.com/book/ch2-7.html#Git-Aliases>`_). This is optional, but I like checking the status to see which branch I'm working on and which files will be included in the next commit.

::

	# On branch master
	# Untracked files:
	#   (use "git add <file>..." to include in what will be committed)
	#
	#	.doit.db
	#	1.txt
	#	README.txt
	#	cache/
	#	conf.py
	#	conf.pyc
	#	conf.py~
	#	files/
	#	galleries/
	#	listings/
	#	new_site/
	#	output/
	#	posts/
	#	stephanieahiga.wordpress.2013-05-05.xml
	#	stories/
	nothing added to commit but untracked files present (use "git add" to track)

Right now there's "nothing added to commit," meaning the local repository is empty. This is because you've just initialized it.

Start tracking your files
=========================

Next, add version control tracking to your files. To add individual files, write ``git add`` and then the filename. To add everything in the directory to your commit::

	git add .

Now it's time to commit the change. The basic commit command is ``git commit``, which will launch your preferred text editor. The ``-m`` flag allows you to skip the text editor and type your commit message inline; the ``-a`` flag tells Git to automatically stage your tracked files, skipping the staging area.

::

	git commit -a -m "Added Nikola site files"

See `Git Basics - Recording Changes to the Repository <http://git-scm.com/book/en/Git-Basics-Recording-Changes-to-the-Repository>`_ for more information on committing changes.

Merge and sync your branches
============================

Merge the remote branch (the GitHub copy of the repository) with your local branch (the local copy of the repository). This consolidates the two branches and ensures that they are identical.

::

	git pull https://github.com/sahiga/sah.git

You should see a message like this:

::

	From https://github.com/sahiga/sah
	 * branch            HEAD       -> FETCH_HEAD
	Merge made by the 'recursive' strategy.
	 README.md |    4 ++++
	 1 file changed, 4 insertions(+)
	 create mode 100644 README.md


**Note:** ``git pull`` automatically merges commits from the "pulled" branch into your current branch. This works fine on an empty GitHub repository, but it could cause `merge conflicts <https://help.github.com/articles/fetching-a-remote>`_.

Push your commit on the local branch to the remote branch::

	git push origin master

If you're using HTTPS, GitHub will prompt you for credentials. To switch to SSH, `follow these instructions <https://help.github.com/articles/why-is-git-always-asking-for-my-password>`_.

	**Note:** I originally attempted ``git push origin master`` before ``git pull``, resulting in a "non-fast-forward" error. This error occurs when the local branch is behind the remote branch, and therefore Git can't push the local commits without losing commits on the remote branch. GitHub has an `article on non-fast-forward errors <https://help.github.com/articles/dealing-with-non-fast-forward-errors>`_ that I wish I'd found when I made this mistake.

The two branches are now in sync! Check the commit history in your local branch with ``git log``. The most recent commit should have a "Merge" attribute, identical to what you'll find in the "Commits" tab in your GitHub account::

	commit e9bcc38554dd930b4bd1f557e45c92f8f65e0a98	
	Merge: 3e653b4 96d590b
	Author: sahiga
	Date:   Sat May 4 23:51:39 2013 -0700

    Merge https://github.com/sahiga/sah

Tutorials for Git and GitHub:

- `Pro Git <http://git-scm.com/book>`_
- `GitHub Help <https://help.github.com/>`_
- `Diary of a Future Dev <http://www.floraworley.com/2013/03/11/get-started-with-git-and-github/>`_

