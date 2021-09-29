# DNA Analyzer - Rachel Blass
The goal of the system is to load, analyze, manipulate and save DNA sequences.

### Description
*DNA sequences are composed of four types of nucleotides;
The nucleotides are marked A (Adenine), G (Guanine), C (Cytosine) and T (Thymine).
A full DNA molecule usually consists of two strands, connected to each other in
base-pair connections: As with Ts, and Cs with Gs.*

The system will interact with the user through a **CLI** (Command Line Interface) that
uses the standard I/O. Using that interface, the user will be able to **load** DNA
sequences from **files**, to **analyze** them, to **manipulate** them (e.g., by extracting
sequence slices or by modifying the sequence), and to **store** modified sequences and
reports.
The commands are detailed in the following sections.


## *project structure*
If we do a short and quick overview of the project structure we will try to do it like this:

All things related to the user interface are inherits from the `CLI` class which implements a simple loop in which to call the `handle_command()` function of the inheriting class.
 
Thus, when we start the program, in the `main()`, we call `CMD()` that it inherits from the `CLI` with prompt `'> cmd >>>' `and every command that comes comes in is managed in the above function.

How?

I again inherited. There is a `Command` class and any class that inherits from it implements the `execute()` function. This is how I can just call the class that is actually the current command I received and call the `execute()` method, without thinking twice ....

### *which disgin patterns I used?*

* **Command** is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request. This transformation lets you pass requests as a method arguments, delay or queue a request’s execution, and support undoable operations.

in my code - the class  `Command` implements that stand-alone object. each class that inherits from the Command class must implement the `execute()` method. so that - in order to execute any command you can simply call the `execute()` method :smile:

* **Decorator** is a structural design pattern that lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors.

in my code - there is the abstract class `CLI`, and you can use all the versions of CLI: Batch, CMD or Confirm.
all of these options are using the `start()` method.

* **Abstract Factory** is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.
 
in my code - the hirarchy in the commmands:

the class Commmand is the base class. some commands like `new` inherits from this class, and some classes inherit from another class inherent in the `Command `class. like `FindCommand` inherts from `Command` and `RegularFindCommand` from `FindCommand`.


***

## *Now let's go over the commands*:
in order to understand the commands it is important to understand the common CLI markings.
### Common CLI markings:
- **[argument]** - Words starting with "[", ending with "]" represent optional
arguments.
- **< argument >** - Words starting with "<", ending with ">" represent required
arguments.
- **arg1|arg2** - Pipe sign ("|") between words represents that each one of them can
be used.

## Sequence Creation Commands:
###  - **new** command:

```
> cmd >>> new <sequence> [@<sequence_name>]
```

creates a new sequence, as described by the followed sequence.

If the `@<sequence_name>` is used, then this will be the name of the new sequence.

Otherwise, a default name will be provided - `seq1` (or `seq2`, `seq3` and so on, if the
name is already taken).
The new sequence, its name and its number (internal ID, starting with 1) are
printed.

*For Example:*
```
> cmd >>> new ATACTGCCTGAATAC @short_seq
```
will create that sequence;

if this is the first sequence, it will be numbered "1" and the following will be
printed:
```
[1] short_seq: ATACTGCCTGAATAC
```


###  - **load** command:

```
> cmd >>> load <file_name> [@<sequence_name>]
```

loads the sequence from the file, assigns it with a number (ID) and a default name, if
one was not provided (based on the file name, possibly postfixed with a number if the
name already exists), and prints it.

###  - **dup** command:

```
> cmd >>> dup <seq> [@<new_seq_name>]
```

duplicates the sequence.
If a new name is not provided, then it will be based on the name of `< seq>`, suffixed
by `_1` (or `_2`, `_3`, ... if the name is already taken).


## Sequence Manipulation Commands:
###  - **slice** command:

```
> cmd >>> slice <seq> <from_ind> <to_ind> [: [@<new_seq_name>|@@]]
```

Slices the sequence, so that starts in `<from_ind>` (0-based index) and ends in `<to_ind>`
(inclusive).

If `@<new_seq_name>` is provided, the results will create a new sequence with that name.
If `@@` is provided, the results will create a new sequence with auto-generate name,
based on the name of the original sequence, with the suffix `_s1` (or, if that name is
already occupied, with the suffix `_s2`, and so on).

###  - **replace** command:

```
> cmd >>> replace <seq> <index> <new_letter> [: [@<new_seq_name>|@@]]
```

replaces the letter in the (0-based) index of `< seq>` by `<new_letter>`.

If `@<new_seq_name>` is provided, the original sequence is left untouched and the
result is put in a newly created sequence with that name.
If `@@` is provided, the name is based on the original sequence, with the suffix `_r1` (or,
if that name is already existing, `_r2` and so on).
The command might get more than a single replacement. In that case, after `< seq>`
there will be more than one pair of `< index>` and `<new_letter>`.


## Sequence Management Commands:
### - **del** command:
```
> cmd >>> del <seq>
```
deletes that sequence.

Before deleting it, the user is asked to confirm that:
Confirmation is done by entering `y` or `Y`, Entering `n` or `N` cancels the deletion. Any
other input will result in a message that asks the user again to confirm the deletion.
Once confirmed, the sequence is deleted and a message is printed. Otherwise, a
cancellation message is printed.

*So, a deletion scenario might look like*:
```
> cmd >>> del #23
Do you really want to delete conseq_1_1: ATACTGCCTGAATACAGCATAGCATTGCCT?
Please confirm by 'y' or 'Y', or cancel by 'n' or 'N'.
> confirm >>> x
You have typed an invalid response. Please either confirm by 'y'/'Y', or
cancel by 'n'/'N'.
> confirm >>> Y
Deleted: [23] conseq_1_1: ATACTGCCTGAATACAGCATAGCATTGCCT
```


### - **save** command:
```
> cmd >>> save <seq> [<filename>]
```
saves sequence `<seq>` to a file.

If `<filename>` is not provided, the sequence name is being used.
The filename is suffixed by .rawdna.

## Sequence Analysis Commands:

### - **find** command:
The find command finds a sub-sequence within a sequence.

It has two flavors:
1. Takes an expressed sub-sequence:
```
> cmd >>> find <seq> <expressed_sub_seq>
```
returns the (0-based) index of the first appearance of `<expressed_sub_seq>` in
the sequence `<seq>`.

*Thus, for example:*

If sequence `#11` is `AACCTTGGAATTCCGGAA` and we are looking for the
sub-sequence `GG`, it will look like:
```
> cmd >>> find #11 GG
7
```
2. Refers an existing sub-sequence:
```
> cmd >>> find <seq_to_find_in> <seq_to_be_found>
```
*Thus, for example:*

If seq `#11` is as appears above, and sequence `#25` is `CTTGGA`, it might look like:
```
> cmd >>> find #11 #25
4
```

### - **findall** command:
```
> cmd >>> findall <seq> <expressed_sub_seq>
```
```
> cmd >>> findall <seq_to_find_in> <seq_to_be_found>
```
work very similar to find, only they return all the indices where the sub-sequence
appears.

*Thus, for example:*

Using the above sequence for sequence `#11`, it might look like:
```
> cmd >>> findall #11 GA
8 16
> cmd >>> findall #11 AA
1 9 17
```

