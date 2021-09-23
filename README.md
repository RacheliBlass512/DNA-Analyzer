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

First of all, common CLI markings
### Common CLI markings:
- **[argument]** - Words starting with "[", ending with "]" represent optional
arguments.
- **< argument >** - Words starting with "<", ending with ">" represent required
arguments.
- **arg1|arg2** - Pipe sign ("|") between words represents that each one of them can
be used.

## Now let's go over the commands:
###  - **new** command:

```cmd
> cmd >>> new <sequence> [@<sequence_name>]
```

creates a new sequence, as described by the followed sequence.

If the `@<sequence_name>` is used, then this will be the name of the new sequence.

Otherwise, a default name will be provided - `seq1` (or `seq2`, `seq3` and so on, if the
name is already taken).
The new sequence, its name and its number (internal ID, starting with 1) are
printed.

$For$ $Example:$
```cmd
> cmd >>> new ATACTGCCTGAATAC @short_seq
```
will create that sequence;

if this is the first sequence, it will be numbered "1" and the following will be
printed:
```cmd
[1] short_seq: ATACTGCCTGAATAC
```


###  - **load** command:

```cmd
> cmd >>> load <file_name> [@<sequence_name>]
```

loads the sequence from the file, assigns it with a number (ID) and a default name, if
one was not provided (based on the file name, possibly postfixed with a number if the
name already exists), and prints it.

###  - **dup** command:

```cmd
> cmd >>> dup <seq> [@<new_seq_name>]
```

duplicates the sequence.
If a new name is not provided, then it will be based on the name of `< seq>`, suffixed
by `_1` (or `_2`, `_3`, ... if the name is already taken).


## Sequence Manipulation Commands:
###  - **slice** command:

```cmd
> cmd >>> slice <seq> <from_ind> <to_ind> [: [@<new_seq_name>|@@]]
```

Slices the sequence, so that starts in `<from_ind>` (0-based index) and ends in `<to_ind>`
(inclusive).

If `@<new_seq_name>` is provided, the results will create a new sequence with that name.
If `@@` is provided, the results will create a new sequence with auto-generate name,
based on the name of the original sequence, with the suffix `_s1` (or, if that name is
already occupied, with the suffix `_s2`, and so on).

###  - **replace** command:

```cmd
> cmd >>> replace <seq> <index> <new_letter> [: [@<new_seq_name>|@@]]
```

replaces the letter in the (0-based) index of `< seq>` by `<new_letter>`.

If `@<new_seq_name>` is provided, the original sequence is left untouched and the
result is put in a newly created sequence with that name.
If `@@` is provided, the name is based on the original sequence, with the suffix `_r1` (or,
if that name is already existing, `_r2` and so on).
The command might get more than a single replacement. In that case, after `< seq>`
there will be more than one pair of `< index>` and `<new_letter>`.


