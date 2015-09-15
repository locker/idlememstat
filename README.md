idlememstat
===========

This is a simple utility for estimating idle memory size. A memory page
is considered idle if it has not been accessed for more than the given
amount of time. Knowing a workload's idle memory size can be used for
estimating its working set size (wss).

`idlememstat` will scan memory periodically, count pages that has not
been touched since the previous scan, and print this information to
stdout. To ease estimating the idle memory size of a particular
workload, this information is gathered and reported per memory cgroup so
that one can put the workload of interest to a memory cgroup and filter
the output of `idlememstat` accordingly. To avoid CPU bursts, each scan
performed by `idlememstat` is evenly distributed in time.

Note, `idlememstat` does not consider unused mlocked pages as idle.

Prerequisites
-------------

0. Linux kernel with `CONFIG_IDLE_PAGE_TRACKING` set (4.3+ required)
0. `g++` with c++11 support
0. `python-2.7` + devel package
0. memory cgroup controller must be mounted under
   `/sys/fs/cgroup/memory` (this is what systemd normally does)

Installation
------------

```
python setup.py install
```

Usage
-----

```
idlememstat [delay]
```

`delay` (equals 300 if omitted) is time, in seconds after which a page
will be considered idle if not accessed by a userspace process.

Output format
-------------

Example:

```
cgroup                   total      idle      anon anon_idle      file file_idle
/                       166436    117720     78772     51728     87664     65992
/test                   114072     85084      5152         0    108920     85084
/                       166488    158916     78824     63596     87664     95320
/test                   114072    114072      5152      5152    108920    108920
```

* `cgroup` - relative path to memory cgroup
* `total` - user memory size, in kB
* `idle` - idle user memory size, in kB
* `anon` - anonymous memory size, in kB
* `anon_idle` - idle anonymous memory size, in kB
* `file` - file memory size (both mapped and unmapped), in kB
* `file_idle` - idle file memory size (both mapped and unmapped), in kB
