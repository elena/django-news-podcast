Title: Django News Podcast 26-Jan-2014
Date: 2014-01-26 00:00
Tags: show-notes
Slug: 2014-01-26-django-news-podcast


---

To modify this file please update the *.md file in the `/content/` directory for changes to be reflected by pelican/gh-pages.

```

| TODO LIST
|
| [x] Fix dates in title above
| [x] Adding releases
| [ ] Security Updates (if exists)
| [ ] Closing Dates
| [ ] Releases
| [ ] Update News from blog
| [ ] (amorphous "Other News")
| [ ] Conference/Event listing
| [ ] UGs, check: http://www.meetup.com/find/?keywords=django&radius=Infinity, http://www.djangonauts.org/
| [ ] (amorphous Community requests)
| [ ] Show notes link
| [ ] Django Dev List summary
| [ ] Credits
| ---
| Other checks:
| [ ] Check all dates replaced
| [ ] Check for any significant at: http://www.planetdjango.org/
| [ ] Check or add links
| [ ] Check all names in credits
| ---
| Posting
| [ ] Recording editing OK?
| [ ] Recording sound level consistent?
| [ ] All items checked off
| [ ] Upload to soundcloud
| [ ] Move from 'drafts' to 'content'
| [ ] Tweet
| [>] Delete this list

```





---

Welcome to Django's News and Updates podcast, the accompanying podcast to Django's blog and update email.

These are the update for the 28 days up to 26th January 2014

	The latest official version of Django is 1.6.1.
	The current production versions of Python are 2.7.6 and 3.3.3.

## 1. Upcoming cut-off and closing dates

(things that are happening in the next 4 weeks)

01-Feb-2014 DjangoCon Europe -- Call for speakers closes 1st February 2014
07-Feb-2014 Django Weekend Cardiff
22-23 Feb 2014 PyCon Philipines

## 2. Releases

### Minor Releases ##

Django 1.7 alpha 1 released
As part of the Django 1.7 release process, today we've released Django 1.7 alpha 1, a preview/testing package that represents the first stage in the 1.7 release cycle and an opportunity for you to try out some of the changes coming in Django 1.7.

Django 1.7 will bring several major new features to Django, along with a host of other improvements. Highlights include a schema-migration framework, a new validation tool to help identify and fix common errors, a complete refactoring of how Django identifies and loads applications, and support for custom database lookups.

For full details, see the in-development 1.7 release notes.

As with all alpha and beta packages, this is not for production use. But if you'd like to take some of the new features for a spin, or to help find and fix bugs (which should be reported to the issue tracker), you can grab a copy of the alpha package from our downloads page. And as always, signed MD5 and SHA1 checksums of the 1.7 alpha package are available.

In addition to the changes covered in the release notes, there are two already-noted issues to be aware of when using the 1.7 alpha package:

Issue #21856 -- an empty value for the DATABASES setting will cause a crash.
Issue #21831 -- using the contenttypes package or GenericForeignKey will fail unless django.contrib.auth is in INSTALLED_APPS.
Both of these will be fixed prior to the final 1.7 release.

Additionally, users of South (a popular third-party package for schema migrations) should note that South is not compatible with the 1.7 alpha.

Posted by James Bennett on January 22, 2014

[Interview with Andrew Godwin]

## 3. News

_[### Post Title]_

Posted by _[Post Author]_ on _[Month D, YYYY]_

_[Post]_


### Other News

_[Any other news]_

"I have a big announcement: at the end of 2013, I married @pydanny. I'm so happy & proud to be with my new husband."

10-Jan-2014
"Just ordered the very first proof of Two Scoops of Django 1.6. Should arrive on Monday. Wahoo!"


Adrian and Jacob retiring as Django BDFLs
Written by Adrian Holovaty on January 13, 2014

Adrian said:

> Since July 2005, when Django was open-sourced, Jacob Kaplan-Moss and I have been the two Benevolent Dictators For Life (BDFLs) of the project. Today we're both retiring from our formal BDFL roles, given that (1) we don't have the time for it that we once had and (2) Django is in great shape with a vibrant community of contributors.
>
> "If you're a Django user, though, have no fear. Honestly, this title seems like a big change "on paper," but in reality it won't change much. "
>

Jacob said:

We reject kings, presidents and voting. We believe in rough consensus and running code.

—The Tao of the IETF


>For me, this has been a long time coming — I’ve been thinking about this for at least a year. In many ways, I this is a similar to a lot of the changes we’ve made over the years: it’s a formalization, and a naming, of what’s already happened. It’s clear to me I don’t have the sort of day-to-day involvement that I once had,

## 4. Conferences/Events

Django sprint in Amsterdam, The Netherlands
We're very happy to announce that a two-day Django sprint will take place on February 22-23 in Amsterdam, Netherlands. This event is organized by the Dutch Django Association.

The venue is the office of TravelBird in the center of Amsterdam. The sprint will start on Saturday, February 22rd at 10:00 CET and and finish on Sunday, February 23 around 22:00 CET.

With the help of the Django Software Foundation and the Dutch Django Association we will have two core developers on site: Baptiste Mispelon and Daniele Procida. Daniele will also be doing his famed “Don’t be afraid to commit” workshop, which will take people new to contributing to Django through the entire contribution process with real tickets. So please don’t hesitate to join even if you’ve never contributed to Django before.

The first beta for Django 1.7 should come out shortly after the sprint, so we can still contribute bugfixes to it.

If you’re unable to come to Amsterdam, you're welcome to contribute to the sprint online. Sprinters and core developers will be available in the #django-sprint IRC channel on FreeNode.

We hope you can join us and help make the sprint as successful as possible!

Posted by Russell Keith-Magee and Erik Romijn on January 23, 2014


DjangoCon Europe 2014: tickets are now on sale
Tickets for DjangoCon Europe 2014, which will be held on the Île des Embiez, are now on sale!

There's an initial run of 50 early tickets, after which prices will go up.

What's different this year is that all tickets include your accommodation and your meals.

It can be a hassle to book suitable accommodation in a place you don't know well, never mind try to work out a budget in advance for your meals and other expenses.

Now consider that this year's DjangoCon Europe will take place on the French Riviera - a gorgeous place to stay, but not exactly noted for being an inexpensive place to visit.

This year, you don't need to worry about finding suitable and affordable accommodation, or where to eat or how much it will cost, because we have taken care of it for you.

As well as saving you the time and trouble of doing it yourself, this will make it much less expensive than it would otherwise have been, because we've been able to negotiate all these prices on your behalf.

So, the basic cost for the event, including two nights' accommodation, two breakfasts, three lunches and two evening meals is a mere €610 at the early bird rate (and only €670 thereafter).

Users Group As anyone who is familiar with the French Riviera can tell you, that's very good value, and it includes the entire conference too!

On top of the basic ticket there are various options:

Early arrival
If you prefer to arrive on Monday afternoon or evening rather than Tuesday morning, you can purchase an extra night (dinner and breakfast included of course).

Sprints
Sprinters should purchase a ticket for the extra two nights and four meals.

Partners and family
Finally, it's not often that one gets to visit a place as special as the Île des Embiez, so make the most of it. You're invited to bring your partner and family!

The island has beaches, nature reserves, sporting facilities, some splendid wildlife - and there are no cars on the island, so it's a lovely environment.

Your partner can join you by purchasing the appropriate Companion ticket. There's no charge for children under four. We're working out prices for older children.

We often talk of the Python/Django family or community, but we're really serious about embracing a wider community - let's make this DjangoCon a truly inclusive family affair!

Djangonaut couples
If both you and your partner wish to attend the conference, you should register as an Attendee and Companion, rather than purchasing two full tickets. Note that this is aimed at couples, and that only double beds are provided.

Posted by Daniele Procida on December 31, 2013

_[### Post Title]_

Posted by _[Post Author]_ on _[Month D, YYYY]_

_[Post]_


Django Weekend Cardiff <https://djangoweekend.org/> is completely sold out.

Our open day remains open however, and you're invited to attend the numerous talks, tutorials and demonstrations in the programme.

<https://djangoweekend.org/tutorials-demonstrations/>

There are fifteen different sessions in the open day programme, on all kinds of subjects. We may even be able to squeeze in a few more over the coming days.

All the sessions are free, and refreshments will be provided.

Registration is required so we know how many people to expect, and places in tutorials will be limited.

The sooner you register the better it is for us, because we have to plan catering, access and other practicalities - so please do it as soon as you can!

Register: <https://djangoweekend-open-day.eventbrite.co.uk>

One of the purposes of the open day is to showcase Django and Python to the local community - developers, researchers, government and business, school pupils and teachers.

We are extremely grateful to the sponsors and supporters of Django Weekend <https://djangoweekend.org/sponsors/>, because they have made this open day possible, and to the numerous speakers and instructors who are presenting these sessions.


#### Other Conferences/Events

Jan 29 Wed  6pm  - *London* @ Conversocial, Epworth House, London
Jan 29 Wed  7pm  - *Washington DC* @ Sunlight Foundation, Washington (48 rsvps)
Jan 30 Thu  5pm  - *Seattle* @ Espresso Vivace Alley 24, Seattle (weekly on Thursday!)
Feb 03 Mon  7pm  - *Houston* @ Stag's Head Pub, Houston
Feb 04 Tue  7pm  - *Dallas* @ rewardStyle, Dallas
Feb 06 Thu  4:45pm  - *Israel* @ Desti Offices, Tel Aviv (65 rsvps so far!)
Feb 06 Thu  6pm    - *Melbourne* @ Common Code, Abbotsford
Feb 06 Thu  6pm  - *Bogotá* @ Atom House, Bogotá (37)
Feb 08 Sat  11am   - *Pheonix* @ Local Motors, Chandler
Feb 12 Wed  5:30pm  - *Silicon Valley* @ Webnertia, San Jose
Feb 18 Tue  7:15pm  - *Los Angeles* @ Metacloud, Inc., Pasadena
Feb 18 Tue  7pm  - *Berlin* @ ... (needs location, has Jannis Leidel)
Feb 19 Wed  7pm  - *Saint Paul Minneapolis* @  Common Roots Cafe, Minneapolis
Feb 20 Thu  7pm  - *Shanghai* @ Lighthouse. Jingan District, Shanghai  (first ever! 6 attendees so far!)
Feb 20 Thu  6pm  - *Bath and Bristol* @ Potato, Bristol (check date with Bath and Bristol Users Group)
Feb 22 Sat  10am  - *Amsterdam* @ TravelBird Amstredam (31)


 - 2014 Apr 9-17 -- PyCon 2014, Montreal Canada (early bird sold out)
   - 2014 Apr 9-10 -- Tutorials
   - 2014 Apr 11-13 -- Conference
   - 2014 Apr 14-17 -- Sprints
 - 2014 May 13-17 -- DjangoConEU, L'île des Embiez is located on the Côte d'Azur, between Toulon and Marseille. (no tickets announced yet, should be this week)
 - 2014 Jul 21-27 -- Euro Python 2014 in Berlin Germany. (no tickets announced yet)
 - 2014 Aug 1-5 -- PyCon AU
 - 2014 Labor-Day weekend September -- DjangoCon 2014, Portland Oregon

http://www.pyvideo.org/

## 5. Community requests/Call outs

_[### Post Title]_

Posted by _[Post Author]_ on _[Month D, YYYY]_

_[Post]_


12-Jan thread
Class based lookups -- Anssi, new #16187 pull#2019 -- documentation needs work, install 1.7a take them out for a spin, add to our docs!

    from django.db.models import Lookup, Extract
	_[define your custom lookup]_

	_[register]_


### Django Updates

If you have any community requests for volunteers, support, sponsorship or other projects, please email [scoop@djangoproject.com](scoop@djangoproject.com) to be posted here.

Sentry 6.4.4 29-Dec
Pillow 2.3.0 is out 1-Jan
Django Extensions 1.3.0 7-Jan
Django Debug Toolbar 7-Jan


New series of posts from PyDanny about using `pytest`.

Did you know?
As of 1.6, Django supports persistend DB connections. They're disabled by default, and can be enabled per-DB in your DATABASES setting.

Turning this on can save you some time at the beginning of every request. The time varies, depending on which DBMS, if you're using SSL, and the latency between your DB server and app servers, but I've seen measurements between 25ms and 450ms.

For more details see the docs.

Did you know?
You can use F expressions in your model fields, not just in filter() statements.

So, if you want to increment an integer field on your model, but want to avoid the obvious race condition, you can use:

>>> from django.db.models import F
>>> product = Product.objects.get(name='Venezuelan Beaver Cheese')
>>> product.number_sold = F('number_sold') + 1
>>> product.save()
For more detail, see Updating attributes based on existing fields.

### Show Notes

These show notes are "open source" on github so please be sure to make any corrections or additions at: [github.com/elena/django-news-podcast](https://github.com/elena/django-news-podcast/blob/master/9999_2013-12-29.md)

Added todo list


## Lastly: Summary of Django Dev this month

Brief and loose summary of what was discussed on the Django Development mailing list during the last 28 days (excluding announcements and support enquiries).

The purpose of this section is to provide a summary of what's been discussed in case something you're particularly interested in.

This is very much a summary so please read and contribute to the actual threads if there's anything mentioned in your field of interest.

This last few weeks was dominated by talk about the new release features.

Particularly the 5 big features going in to 1.7:

- Schema-migrations
- App refactor
- Custom lookup
- Advanced pre-fetching
- Validations

There was also interesting discussion _[...]_


#### _[D-Mmm-YYYY Verbatim Title of Thread]_

_[Thread First Author]_

_[Related Ticket: #nnn Verbatim title of ticket (ticket status)]_

_[Summary of post]_

_Add verbatim quotes:_ <br>
_> quote_ <br>
_> quote_


## C



# (1) Re: python-social-auth partial pipeline can not resume |Jan 11 By Karen Tracey 1 post 25 views
# (2) New to Django - Question: All registered users to post content... |Jan 6 By Retnuh 2 posts 49 views
# (3) Consider reopening ticket #11385 |Jan 8 By Andres Osinski 3 posts 70 views
# (3) django_bash_completion in Pypi Package |Jan 7 By Brett Nekolny 3 posts 74 views

## Big Features


## Clarification of workings

(1) Django sprint in Amsterdam, The Netherlands, Feb 22/23 |Jan 23 By Erik Romijn 1 post 24 views
(1) Fixing #10811 Prevet assigning of unsaved model to Foreign Key |Jan 25 By anubhav joshi 1 post 20 views
# (1) Re: Django doesn't give any feedback if it cannot connect to a DB |Jan 11 By Ramiro Morales 1 post 35 views
(1) Saving deleted code from Django source code |Jan 6 By Vajrasky Kok 3 posts 117 views

(2) Merging GSoC 2013 - Validation Refactor |Jan 20 By Russell Keith-Magee 2 posts 78 views
# (2) Patch fix for #21430 : Exception to be raised when unpickiling QuerySet across unsupported django version |Jan 18 By Prasoon Shukla 2 posts 44 views
(2) Self-referenced template recursion handling |12/30/13 By unai 26 posts 251 views
(2) [ANNOUNCE] Django 1.7 alpha 1 released |Jan 23 By James Bennett 2 posts 53 views
# (2) permit global change of BaseForm.label_suffix |Jan 15 By Tilman Koschnick 2 posts 49 views

# (3) Consider allowing customization of ModelForm's init parameters in contrib.admin |Jan 16 By tyrion-mx 3 posts 43 views
# (3) Re: Digest for django-d...@googlegroups.com - 1 Message in 1 Topic |Jan 3 By shmengie 3 posts 50 views
# (3) Should exceptions in dev server appear as tracebacks in the console by default? |Jan 16 By Harry Percival 3 posts 93 views
(3) django.core.checks.register shouldn't be (primarily) a decorator |Jan 23 By Shai Berger 3 posts 44 views
# (3) python querry on firebug extention . |Jan 13 By JAI PRAKASH SINGH 3 posts 41 views

(4) Quick question re typo-fixing etiquette |Jan 25 By James Turley 4 posts 43 views
(5) Is it a mistake on docs for django 1.5? |Jan 21 By Leonardo Borges Avelino 5 posts 51 views
(5) Website integrated mobile app for disaster |Jan 12 By unk...@googlegroups.com 5 posts 87 views

(8) Ticket #21751 review requested |Jan 22 By Michael Manfre 8 posts 98 views
(10) Feature request: post/pre commit/rollback signals |Jan 19 By Jesús Espino 10 posts 137 views

#21803 new New feature
Support post-commit hooks

This allows attach some code when a transaction is committed or rolled back.

only when a transaction is committed successfully

Carl Meyer
https://github.com/carljm/django-transaction-hooks

(10) Feature request: serve_file() view in static app |Jan 20 By Rivo Laks 10 posts 111 views

(13) 1.7 Schema migrations and AUTH_PROFILE_MODULE / get_profile() deprecation |Jan 25 By Brian Neal 13 posts 71 views
(13) Must a Django Database Support Migrations? |Jan 23 By Michael Manfre 13 posts 89 views


(17) Enforce the use of a unicode string in settings.LANGUAGES |Jan 23 By Henrique Romano 17 posts 78 views
(17) Recommending a Python 3-compatible MySQL connector |Jan 23 By Aymeric Augustin 17 posts 1644 views

(3) CAS in cache framework |Jan 18 By Alexey Moskvin 3 posts 51 views
Compare-And-Set in Memcache
django cache api doesn't support. Patches welcome.

(8) Thoughts on defining and autoimporting signals.py |Jan 16 By Daniel Sokolowski 8 posts 396 views
Daniel Sokolowski 22-Dec-11
Asking about where to define signals for an app. Back then the word from RKM was:

> The root problem is that there isn't a single reliable place to put "app startup" logic. With the current way Django handles apps, there isn't a single solution that will work everywhere, which one of the reasons that the docs are silent on the issue.

Coincidentally this thread was re-dug up on 15-Jan, and Aymeric could promptly state that "It's fixed in 1.7" and point to both 'signals' in the docs and to the app refactor commits and discussions.

https://github.com/django/django/commits/master/docs/ref/signals.txt

So for the record folks:

As at 1.7 there is an official, "Django way" for where to put signals, where to put handlers, where to wire them up, and how to test all that stuff.

There's a commit from Aymeric called: "Updated advice on connecting signals at startup."

(2) Class based lookups |Jan 12 By Anssi Kääriäinen 2 posts 46 views
Class based lookups -- Anssi, new #16187 pull#2019 -- documentation needs work, install 1.7a take them out for a spin, add to our docs!

    from django.db.models import Lookup, Extract
	_[define your custom lookup]_

	_[register]_

(12) Migrations and swappable models/AUTH_USER_MODEL |Jan 12 By Andrew Godwin 12 posts 123 views

Long and technically deep discussion about applying "swappable models" migrations. A major feature of 1.7

Swappable models are an interesting and powerful feature.

(16) Renaming apps.has\_app |Jan 7 By Aymeric Augustin 16 posts 90 views
The hardest of problems: naming things.

> During the app_loading refactor, I introduced a method to test if a given application is enabled, and I named it `has_app`.

Its main uses are detecting misconfigurations and skipping tests.

Tried: .installed .has\_app .has\_installed .have\_installed

_is\_installed_

(6) Forbidding double imports |Jan 7 By Aymeric Augustin 6 posts 101 views

Up to Django 1.4: every Django project was vulnerable to double import problems: since PYTHONPATH contained both a directory and its parent, the same module could get imported twice through different paths.

As of Django 1.6: there’s no built-in support for setting PYTHONPATH like that. However, some users may still be setting it manually to avoid fixing their imports.

Django still contains some ad-hoc mechanisms to work around the consequences of this poor setup, notably
ModelBase, the metaclass for Model: defining a class that inherits from Model can return an existing class instead of creating a new one.

He'd be inclined to do it immediately, shouldn't be too hard, but being *not backwards compatible* will create deprecation path to 1.9.

As the incompatible behaviour predates the LTS version 1.4 (to paraphrase Last comment on 7-Jan): Double imports will be killed with fire.


(19) Improving aggregate support (#14030) |Jan 20 By Josh Smeaton 24 posts 399 views
Josh Smeaton has taken on the challenge of #14030 - to allow using more complex expressions in aggregates.

This one's been on the cards for 3 years now, and a number of people have looked into it. With Anssi Kääriäinen (akaariai) lending advice, perhaps we can hope to see this land soon!

(24) App-loading: Pragmatic concerns about default AppConfig objects and ready() implementations (24) |Jan 25 By Russell Keith-Magee 24 posts 178 views


(31) App-loading reloaded |Jan 14 By Aymeric Augustin 47 posts 804 views
Aymeric Augustin has very publicly worked on the App Loading refactor, giving a detailed plan at the start, regular updates, and a slew of code improvements.

This work has focused on changing how we think about INSTALLED_APPS. The most noticeable changes are:

Allow apps without a models module or package
Provide a verbose name, for example for the admin
My personal favourite goal "Provide a reliable initialization signal" was, unfortunately, not achieved in the time frame, but looks to be within sight. All of the resulting tasks are now in tickets with the keyword "app-loading", ready for the wider community to tackle.



#### Django Security & OWASP Project |Jan 20 By Michael Coates 2 posts 113 views
Jan 15 Michael Coates

He says:
Over at OWASP they've started a framework security project. His goal is to capture the security posture, options and capabilities of different frameworks.

When I was leading the security team at Mozilla we worked with Django a ton.

When I was leading the security team at Mozilla we worked with Django a ton. You guys have always been on the leading edge of framework security. It was an easy choice to start with Django for the OWASP framework security project.

To which JKM (head of security at Heroku and former Django BDFL) replies:
This sounds right up my ally. I'll jump on the list and post some more info over there.

They're looking for help:
- reviews their list of security controls in frameworks (which will become a "standard list")
- assistance with adding missing controls

If you're interested join the mailing list, google: OWASP framework security project


## SMALL STUFF

(3) Schema editor changes feedback request |Jan 6 By Michael Manfre 3 posts 59 views
MSSQL


(#21340) Using setuptools to make django-admin.py runnable on Windows |12/30/13 By Remram 15 posts 215 views
Using setuptools
The idea of using setuptools to make django-admin.py runnable on Windows (#21340) has been brought up again.

After discussion on IRC, the following was decided (as posted by Florian Apolloner):

We are not going to support setuptools and distutils, this makes the setupprocess difficult to debug and test imo.
Given Donald's "okay" we might switch to setuptools completely
There seems to be a bug in pip when installing a wheel, which renders the django-admin.exe unusable on windows, help welcome
PR for this issue is now at https://github.com/django/django/pull/2116


#### Testing parameters in database settings
Jan 20 By Shai Berger 7 posts 65 views

Ticket: \#21775 No facility to specify the datafile of a django test Oracle tablespace (assigned New feature)
State: ongoing discussion about what an appropriate way of organising a solution to this might be in settings.

Last and slightly least:
# (1) Proposal of (another) podcast |12/29/13 By me 1 post 210 views
