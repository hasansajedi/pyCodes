# Python Generators

## What is a Generator?
> A Python generator is a function that produces a sequence of results. It works by maintaining its local state, so that the function can resume again exactly where it left off when called subsequent times. Thus, you can think of a generator as something like a powerful iterator.

The state of the function is maintained through the use of the keyword yield, which has the following syntax:

``` python

yield [expression_list]

```

This Python keyword works much like using return, but it has some important differences, which we'll explain throughout this article.

Generators were introduced in PEP 255, together with the yield statement. They have been available since Python version 2.2.

