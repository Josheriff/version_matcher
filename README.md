# Version Matcher

Tells you wich packages are outdated in your python project

## Mental Roadmap

First of all, all this script must be coded using TDD style.

Is the second attemp, the first one was cool to learn but this attemp to do the same but with the learned lesson from the bicha

## Arquitecture reflexions

First time we tried to let the tests to guide us to the "perfect" arquitecture

after some investigations, we learnt that TDD can guide you, but you must think your arquitecture, if its bad the tests will tell you
if your arquitecture is good, the tests will not hurt ;)

## Arquitecture

I gonna part this script in four parts, described in order of actuation:

- *File reader:*

Will look for every "dev-dependencies.txt" and "dependencies.txt" files, storage each file into an array

- *Repo reader:*

Will look for every dependency storaged in the file reader array described before, and storage the version in other array

- *Version matcher:*

Will compare the File reader array and the Repo reader array, and generate an object

- *Render:*

Will use the Version matcher object to show the results in different ways (most basic first iteration)
