# Click Tutorial

## Introduction
Things that a command line application needs to be able to do:

*Why?*
Allow people to use our application in ways that people didn't expect.

*WHy write clis?*
* Tasks that need to be automated/scripted.
* Management interface for larger application

*Why python?*
* Lots of vendors with python sdks.

*Why click?*
click.palletsprojects.com/why/
* Encourage standards and norms of command line applications
* Has some helper features that you'd otherwise need to implement yourself (progress bars, colored prompts)

## Well Behaved CLI Interface

### Arguments and options
*arguments* - Required information that is passed to cli

*options* - Optional. Keyword, flag

### Write to `stdout`/`stderr` and read from `stdin`

### Exit codes
Exit with 0 if successful, non-zero if failed.

### Ctrl-C / Signals
Long-running application should be able to handle signals and keyboard interrupts (i.e. Ctrl+C)

### Configuration / State information
Different per OS. Should store data in the correct place based on the operating system.

### Colors
Helps to make the Command-line interface more meaningful.

However, it's important to behave differently when run interactively vs taking output and piping to another program.

## Intro to Click ([Click Documentation](click.palletsprojects.com))
Click uses decorators.
When you use
```python
@click.option('--count')
def hello(count)
    print(count)
```

The value of `--count` will be passed to the decorated function as a keyword argument. This means that you need the argument name `count` in `@click.option` to match up with the argument name `count` in `def hello(count)`.

This means that the following code will fail?
```python
@click.option('--count')
def hello(number)
    print(number)
```
### Input Validation




