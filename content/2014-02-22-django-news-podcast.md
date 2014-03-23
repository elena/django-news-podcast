Title: Django News Podcast 22-Feb-2014
Date: 2014-02-28 00:00
Tags: show-notes
Slug: 2014-02-22-django-news-podcast


---

| Posting
| [ ] Recording editing OK?
| [ ] Recording sound level consistent?
| [ ] All items checked off
| [ ] Upload to soundcloud
| [ ] Move from 'drafts' to 'content'
| [ ] Tweet
| [>] Delete this list from this file and publish notes

Recording Meta data:
Artist Name: Django News Podcast with _[Elena Williams]_
Track Title: D-Mmm-YYYY Django News Podcast
Album Title: Django News Podcast YYYY
Year: YYYY
Genre: podcast, technology, programming, python, django
```

---

Welcome to Django's News and Updates podcast, the accompanying podcast to Django's blog and update email.

These are the update for the 28 days up to 22-Feb-2014


    The latest official version Django is 1.6.2.
    The current production versions of Python are 2.7.6 and 3.3.4.


This podcast provides brief coverage of the current activity in the Django community.

In this edisode I'll be talking about:

- New releases and going over some of the features in large  upcoming 1.7 release.
- I talked to ** both Russell Keith-Magee and (amm) Aymeric Augustin about the `App-loading refactor` one the most interesting big features in the new releases.
- News
- Dev List Summary


## 0. Security

There were no obviously Django-spe

// pass # 1. Upcoming cut-off and closing dates
// March 6, 2014	Django 1.7 beta; complete feature freeze.


## 2. Recent Releases

Jacob Kaplan-Moss posted on February 6, 2014 two minor releases

Django 1.6.2

It's the latest bugfix release in the ** 1.6 series, it fixes about a dozen small 1.6.1 bugs.


Django 1.7 alpha 2

There's a second alpha release for Django 1.7 after we discovered a bad interaction between the changes to way apps are loaded and the new system checks framework.
Because these changes made 1.7a1 particularly unstable, we're taking the step of releasing a second alpha.


Announced on 10-Feb:

    ** Python 3.3.4

This release fixes several security and a lot of overall bug fixes found in Python 3.3.3.

Announced on 23-Feb:

Python 3.4.0 release candidate 2
Python 3.4 includes a range of improvements, including hundreds of small improvements and bug fixes. This is not suitable for production environments


### New Non-Django releases:

Selection of popularly used django packages (according to Django packages that recently upgraded themselves), listen out for anything your might use:

    02/02/2014 Raven
    02/13/2014 Django celery
    02/19/2014 Django Model Utils
    02/20/2014 Django Grapelli
    PyCharm 3.1


---

Quick overview of some of major features going  in to 1.7:

##### Schema migrations

 >> As at 1.7 django-south will be obsolete and as its author has re-constructed it in Django core and its currently available for testing.

If you're familiar with South what this means is that:

* `syncdb` no longer exists, this is generally replaced by `migrate`
* the `schemamigration` command is replaced by `makemigrations`
* If you've ever looked the files generated in the `migrations` directory in your app, these have changed too:
  if you open one these it's now a pretty obvious looking class:
  - you can add your own methods in the migration easily
  - and although these files still labelled 0001, 0002 but they don't necessarily have to load in this linear order
  - you can define if a migration depends on another, even if it comes later
  - the frozen state cruft has been taken out

There's also now a setting to change the name of your migrations directory.

If do have a project that currnntly uses south and you want to convert it to the new built-in Django migration
The official way of converting your old project to new is getting everyone who's working your database to the same place in your old migrations, so everyone's schema is the same, then going through and deleting all the migrations directories and running `makemigrations [app]`.

I talked to Andrew Godwin the author of both south and this in the last podcast if you hadn't heard it.

##### App-loading Refactor

I have a couple of interviews about the  refactorR   later, but the most interesting 2 features for day-to-day Django users are:

* Each app can now have an `AppConfig` where you can _change or translate the name of your app_ in admin (which was the original point of the 7 year old ticket that started this)
* You can put your signals in the `AppConfig` for all those folk out there who have been frustrated by not having anywhere decent to keep this logic before.

##### Custom QuerySets

Historically, if you wanted interesting reusable queries on your model the recommended way was to make a custom Manager class -- but seeing as this _returns_ a QuerySet you can't use it to chain custom methods together -- there are work-arounds but they're not dry and they're not pretty.

Now there's a new `QuerySet` class (we all know `models.Model` well now) theres a `models.QuerySet`.

So you make this `models.QuerySet` class and put your filter methods in this class.

Then to connect this with your `models.Model` you set it as the `objects` attribute (people who've used managers before will be familiar), well now you use this `models.QuerySet` class as your manager and you can chain together the filter methods to your heart's content.


##### Custom Lookups

Relatedly there's also a new `Custom lookups` features.

Django ships with a pile of built-in lookups -- this is those `.filter(field__[django inbuilt lookup]`, but say you have something interesting that your database will let you do, say like Geographic data.

Technically doing this has always been possible but you had to know how to do it.
there's a lot of clean syntax at a database level.

Well there are some more new `models.` class: the new `models.Lookup` and `models.Transform` classes.

You can take you SQL-fu out for a spin and construct any database lookups that are specific to your database backend, as an `as_sql` method inside that `Transform` or `Lookup` class that returns a lhs and rhs and some parameters that define you SQL query,

and register them against particular fields.

Thanks for Anssi for this it looks relatively simple for all the complex internal that are shuffled around to maket this happen.

##### Other 1.7 features

There's a new checks Framework which replaces `manage.py validate` and add a bunch of validation options, I talk to Russell Keith-Magee (who committed this to core) about this in the last podcast.

There's new `Prefetch` object you can use for interesting and advanced `prefetch_related` operations.

So you guys know the `Now` and `Today` shortcuts in admin? Well these now use the datetime defined by the `current time zone` rather than browser time, which is used to use (this is different from the `default time zones` you define in your settings obviously).


---


Django 1.6.2 is the latest bugfix release in the 1.6 series, and Django 1.7a2i s the second alpha preview of the upcoming 1.7 release.

Today we're releasing Django 1.6.2, the latest bugfix release in the 1.6 series, and Django 1.7a2, the second alpha preview of the upcoming 1.7 release.

#### Django 1.6.2
Django 1.6.2 is the second bugfix release for the Django 1.6 series. Most bug fixes are minor; you can find a complete list in the Django 1.6.2 release notes.

All users are encouraged to upgrade to Django 1.6.2 at your earliest convenience. You can install Django using pip or download Django 1.6.2 from the Django downloads page. As always signed checksums of the package are available.

#### Django 1.7 alpha 2
Django 1.7 alpha 2 is a preview/testing release that represents the next stage in the 1.7 release cycle. It's an opportunity for you to try out some of the big changes coming in Django 1.7.

We're making a second alpha release for Django 1.7 after we discovered a bad interaction between the new system checks framework and the changes made to app loading. Because these changes made 1.7a1 particularly unstable, we're taking the step of releasing a second alpha.

For full details of what's new in Django 1.7, see the in-development 1.7 release notes.

As with all alpha and beta packages, this is not for production use. But if you'd like to take some of the new features for a spin, or to help find and fix bugs (which should be reported to the issue tracker), you can grab a copy of the alpha package from our downloads page. And as always, signed MD5 and SHA1 checksums of the 1.7 alpha package are available.



---

The next major release of Django is 1.7 scheduled for May 15th.

-  1.7 beta -- March 6th (complete feature freeze)
-  1.7 release candidate -- May 1st (translations freeze)
-  Final release -- May 15th (assuming a second release candidate is not needed)

Andrew Godwin has stepped up to be the release manager for 1.7, he says:

> We will feature-freeze and branch off a release branch as we roll the beta, and any features that aren't in by this date _will_ have to wait.

More details can be found at [Version1.7Roadmap on the wiki](https://code.djangoproject.com/wiki/Version1.7Roadmap).


## 3. News

From Django Updates, Python Weekly email, Django planet.

Revsys
http://www.revsys.com/blog/2014/feb/19/django-debugging-bookmarklet-trick/

---

#### Book: Two Scoops of Django: Best Practices for Django 1.6

Tweet:
Announcing Two Scoops of Django 1.6
Posted by Daniel Greenfeld on January 31, 2014

It's our pleasure to announce that after months of research, writing, and review, Two Scoops of Django: Best Practices for Django 1.6 is in available....


Two Scoops of Django: Best Practices for Django 1.6 is chock-full of even more material that will help you with your Django projects. It introduces you to various tips, tricks, patterns, code snippets, and techniques that we've picked up over the years. This second edition includes over 130 new pages of concise, example-packed text containing 5 new chapters and 3 new appendices.

---

#### Book: Python Pocket Reference
22-Jan

Updated for both Python 3.4 and 2.7, this convenient pocket guide is the perfect on-the-job quick reference. You'll find concise, need-to-know information on Python types and statements, special method names, built-in functions and exceptions, commonly used standard library modules, and other prominent Python tools. The handy index lets you pinpoint exactly what you need.

Python tutorials, Learning Python and Programming Python, also written by Mark.

---

#### Kickstarter: Improved PostgreSQL support in Django
Marc Tamlyn
Supporting a wider range of awesome PostgreSQL features in Django - including hstore, JSON and full text search

Fri 14 March
\>8K

- hstore
- json
- array
- enum
- interval (maps to a timedelta)
- int4range, tsrange and other range fields
- uuid

£5000 - Improved date-based lookups for all databases. This means it will be possible to do lookups like field__year__lte. It will also include other time filters for PostgreSQL, such as __decade and __century.

£7500 - PostgreSQL-specific custom lookups for existing fields, including string and mathematical operations. The new PostgreSQL-specific data types will also now benefit from a wider range of custom lookups.

£10000 - Custom indexes, including different index types (e.g. gin indexes) and functional indexes (e.g. indexing on year of a date field).

£14000 - Support for views (and materialized views) in PostgreSQL and other database backends.

---

### Kickstarter: Try Django Tutorial 21 videos now online
CodingEntrepreneurs
Published on Jan 30, 2014

This Course was Funded on Kickstarter: http://www.kickstarter.com/projects/j...
$54,375

---

## Events

#### PyCon India 2014
September 26-28, 2014

#### EuroPython
Early bird is sold out for EuroPython
Call for volunteers
http://ep2014.europython.eu/en/conference/volunteers/



## Did You Know

Thanks to Curtis Maloney (aka FunkyBob)

#### Did you know?
dashboard.djangoproject.com

#### Did you know?
The {% regroup %} tag doesn't sort your data, so if you're not careful it may produce multiple groups with the same 'grouper' value. However, sometimes you may want this...


## 4. Conferences/Events

#### Other Conferences/Events

 - 2014 Apr 9-17 -- PyCon 2014, Montreal Canada (early bird sold out)
 - 2014 May 13-17 -- DjangoConEU, L'île des Embiez is located on the Côte d'Azur, between Toulon and Marseille. (no tickets announced yet, should be this week)
 - 2014 Jul 21-27 -- Euro Python 2014 in Berlin Germany. (no tickets announced yet)
 - 2014 Aug 1-5 -- PyCon AU
 - 2014 Labor-Day weekend September -- DjangoCon 2014, Portland Oregon

Just past: Django weekend in Cardiff; Django Sprints: Amsterdam and Krakow; PyCon Philipines.


## 5. Community requests

### Django Updates

If you have any community requests for volunteers, support, sponsorship or other projects, please email [scoop@djangoproject.com](scoop@djangoproject.com) to be posted here.

### Show Notes

These show notes are "open source" on github so please be sure to make any corrections or additions at: [github.com/elena/django-news-podcast](https://github.com/elena/django-news-podcast/blob/master/9999_2013-12-29.md)


## Lastly: Summary of Django Dev this month

Brief and loose summary of what was discussed on the Django Development mailing list during the last 28 days (excluding announcements and support enquiries).

This is very much a summary so please read and contribute to the actual threads if there's anything mentioned in your field of interest.

The most notable couple of discussions were:

- GSoC proposals
- 1.7 chatter


#### Feb 20 (10) The unsettings project|By James Farrington 10 posts 255 views
James Farrington Feb-11

>Django modules should work as libraries (e.g. ORM, mail, etc).  "from django.conf import settings" bootstrap undermines this.  unsetting begins a path to support the legacy structure, but still allows for the 'librarification' of Django modules.  Then, we can move on with more options to whether we want to refactor things or not and how.

From a discussion in Chicago with Adrian.

They have a working concept
github/SlashRoot/

Their implementation revolves around replacing settings with a user_settings decorator.


#### (12) Feb 06 changing the on_delete=CASCADE default|By Carl Meyer 12 posts 184 views

\#21127 "on\_delete=models.SET_NULL should be the default for nullable FKs" mid-Sept 2013

> a model instance with a null FK hanging around that you didn't expect to still have, the other way you get data loss



Conversation leapt to
Christophe Pettus

generic relations touch on

\#21961

#### 1.7 (04) Feb 13 Django 1.7 data migrations?|By Kent Engström 4 posts 116 views

Basically pinging for documentation on:
https://docs.djangoproject.com/en/dev/topics/migrations/#data-migrations

(which are doing using the `python manage.py *makemigrations* --empty yourappname` management command.


#### 1.7 (05) Feb 12 Re: Testing 1.7a2 -- pre_migrate and post_migrate (py2.7)|By Val Neekman 5 posts 35 views

Clarifying signals should be put in `AppConfig.ready()`, the documentation has


#### email identification rather than username


#### Feb 22 (03) Using namedtuple instead of pure tuples|By Adam Kaliński 3 posts 21 views
Adam Kaliński Feb-22

Florian suggested preformance impacts be assessed.

Both Adam and Stratos Moros made some `unscientific microbenchmarks` (with a gist).

There are some interesting examples of benchmarking here.

Adam exploring this more.


#### Feb 22 (04) AM should we include images in Django documentation?|By Pieter Marres 4 posts 27 views
Pieter Marres

This comes up occassionally. The perenniel problem with images in docs is figuring out what g

This is *hard* and I don't know if there are any graphics in the Django docs but it seems to occupy that same multiple-skills-required space as fixing the Django admin.


#### Feb 16 (04) Ticket #9?|By Justin Holmes 4 posts 57 views

Ticket #9 'Add transaction support' 5-Jan-2006

It's implemented.

Deleted, in webarchive.


#### Feb 13 (03) bootstrap default admin theme|By adam spence 3 posts 136 views
Adam Spence

django-admintools-bootstrap


#### Feb 13 (03) Migrations and System Checks|By Mark Lavin 3 posts 50 viewsR
Mark Lavin

Short but Ticket #21856 `Crash when DATABASES = {}`

R R  Mark says:
> Upon diving in I saw that the checks for un-applied migrations
> were tied to the runserver command. I thought to myself that this
> seemed more appropriate for the new system checks framework. I assumed that it
> hadn't been done this way originally because Andrew's work on migrations was running
> parallel to the system checks. I figured while I was fixing the issue at hand it
> would make sense to migrate (if you'll excuse the pun) this check to the new framework.

So he converted the current check and put it in to the checks framework.

" a _system issue_"


(Turns out the crash when DATABASES = {}
ImproperlyConfigured)


#### Feb 06 (06) Check Framework Feedback|By guettli 6 posts 70 views

Whether to define an argument `hint` for the Error class. Eg. Error("Error message.", hint=None)

Turned in to a discussion about whether hints to be explicitly omitted to None by default.

Last word was the way to do it properly is for the object to accept **kwargs but this is messy.


#### Feb 04 (03) test_disable_constraint_checks_context_manager|By Wlodek 3 posts 53 views
Wlodek 3-Feb

If you're interested in `disabling constraint checks` in tests, then this is the conversation for you.

Seems to be nutting out using `disabling`/`deferring` contraint checks.

Presumably there are multiple database backends involved.

In the end the OP uses a Try/Except `connection.constraint_check_disabled()`.


#### Feb 04 (03) Django doesn't log much at high verbosity levels|By Chris Wilson 3 posts 97 views

Talks about adding more logging -- goes through the loggidng does and doesn't do.

Russ made 2 points:

* perhaps web server level thing
* be really careful about performance

Chris put in a ticket adding some details: 21949 "doesn't log much at high verbosity levels".


Jan 27 (14) Multi-tenant Django|By Alec Taylor 14 posts 676 views


#### (14) Jan 27 Multi-tenant Django|By Alec Taylor 14 posts 676 views
Alec Taylor MAY 2012

multi clienst per database/"database per client" discussion.

People talk about experiments

`django-simple-multitenant`
`django-multi-schema`

Someone mentions that one db per client is probably easier


#### (02) Feb 04 freenode under DDOS attack -- IRC works on webchat|By Shai Berger 2 posts 78 views

FWIW, it seems that NickServ is also nonfunctional/unresponsive due to
the DDOS, which means that even if you can connect (and I have been able
to connect via IRC client), you won't be able to get into #django,
#django-dev, #django-core, #python, or any other channel that requires
registration.


### Summary of GSoC proposals:

#### gsoc (01) Feb 21 GSOC 2014 Proposal|By Devashish Badlani 1 post 37 views
#### gsoc (02) Feb 06 GSoC Project Ideas|By Cody Scott 2 posts 76 views
#### gsoc (03) Feb 18 Gsoc project idea|By NAVNEET SUMAN 3 posts 82 views
#### gsoc (08) Feb 22 GSOC 2014 Project Proposal|By Devashish Badlani 8 posts 87 views
#### gsoc (10) Feb 20 [GSOC] Improving the Test-Suite|By Akshay Jaggi 10 posts 177 views
#### gsoc (13) Feb 18 GSoC query|By anubhav joshi 13 posts 209 views

Error reporting
Tests
Aggregation/Notation
django.core.serializers
Django Book
 >> New django book due out Apr 15 with Katie Cunningham added to the authors list (according to Apress)



#### gsoc (36) Feb 22 [GSoC] Switching to Jinja2 proposal|By Christopher Medrela 36 posts 495 views

Holy crap this thread is long.
