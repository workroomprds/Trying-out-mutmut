# `mutmut` environment - setting up

installed `mutmut` with package manager
few dependencies than other.

! Some warnings from `setuptools`
`SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.`

From [docs](https://mutmut.readthedocs.io/en/latest/index.html#install-and-run)


`mutmut run` FAILS with 
```
FileNotFoundError: Could not figure out where the code to mutate is. Please specify it on the command line using --paths-to-mutate, or by adding "paths_to_mutate=code_dir" in pyproject.toml or setup.cfg to the [mutmut] section.
```
which seems eminently sensible

I need code, and `mutmut` has opinions on where it should be.

Following docs descripion of config, set up `/src` and `/tests`
```
[mutmut]
paths_to_mutate=src/
backup=False
runner=python -m hammett -x
tests_dir=tests/
dict_synonyms=Struct, NamedStruct
```
From [An introduction to mutation testing in Python](https://opensource.com/article/20/7/mutmut-python)
make `/src/angle.py` and `/tests/test_angle.py` w/ code from page

installed `coverage` and `pytest` packages

Apparently 
```
coverage run `which pytest`
```
But I dunno about that. And it proiduces errors.

I reckon 
`pytest tests/`
Which produces the same errors

add `__init.py__` to tests/

add `from src import angle` to test_angle

now `pytest tests/` works

and ```coverage run `which pytest` ``` doesn't fail (also, doesn\t report coverage)  ... **Ignore for now** 

now, `mutmut run --paths-to-mutate src/angle.py` (note slight variation on page stuff)

```
2. Checking mutants
⠏ 20/20  🎉 4  ⏰ 0  🤔 0  🙁 16  🔇 0
```
Took a while!


`mutmut results`
```
To apply a mutant on disk:
    mutmut apply <id>

To show a mutant:
    mutmut show <id>


Survived 🙁 (16)

---- src/angle.py (16) ----

3-6, 8-13, 15-20
```
I've added several tests
Now, let's see
`mutmut run --paths-to-mutate src/angle.py`
```
2. Checking mutants
⠸ 20/20  🎉 14  ⏰ 0  🤔 0  🙁 6  🔇 0
```

faster, cos not checking killed ones

baselining is slow.

`mutmut results`

These six: 4-5, 11-12, 17-18
* 4: 360 -> 361 ... so a precision test needed
* 5: // -> / .. what is this / returns float, // returns whole

---
### With Bart - 20220623

We dug into this
* Hard to get both at same time - may be a teams interruption
* Observed 360->361 and // -> / , so considered tests
* Precision hard - so used pytest to explore possibilities giving a half degree - change to hour based on min
* // -> / didn't matter (?) as output mde `int`
* took out `int`s **from code**, wrote tests for fractions (aiming to get less-mutatable code)
* extra tests
  * noticed an unfulfilled test - that all numbers should be whole... implied in code, possibility of req. Would a test have 'killed' a mutant?
  * perhaps, if we're going to have consts, we should have tests for thos consts, too. Would that be reasonable?
  * tests for hard-to-calculate numbers (i.e. result in float) - how to find these? Run a few randoms in, pick the odd one, check it, keep it.

---
### JamesFails
! tried to run code from console, not shell

```
File "<stdin>", line 1
    mutmut run
           ^
SyntaxError: invalid syntax
```
Did install fail?
```
 pip install mutmut
  File "<stdin>", line 1
    pip install mutmut
        ^
SyntaxError: invalid syntax
```
...wtf is going on?

---
install stuff
```
Repli: Updating package configuration

--> python3 -m poetry add mutmut
Using version ^2.4.0 for mutmut

Updating dependencies
Resolving dependencies...

Writing lock file

Package operations: 4 installs, 0 updates, 0 removals

  • Installing glob2 (0.7)
  • Installing junit-xml (1.8)
  • Installing pony (0.7.16)
  • Installing mutmut (2.4.0)
/home/runner/Trying-out-mutmut/venv/lib/python3.8/site-packages/setuptools/command/install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
  warnings.warn(
/home/runner/Trying-out-mutmut/venv/lib/python3.8/site-packages/setuptools/command/install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
  warnings.warn(
```