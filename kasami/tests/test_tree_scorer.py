from nose.tools import eq_

from .. import tree
from ..tree_scorer import TreeScorer


def test_pcfg():
    trees = [
        tree.parse("(S (NN 'foo') (VBZ 'bar')))"),
        tree.parse("(S (NN 'foo') (VBZ 'baz')))"),
        tree.parse("(S (NN 'foo') (VP (DET 'a') (VBZ 'baz')))")
    ]

    foo_ts = TreeScorer.from_tree_bank(trees)

    t = tree.parse("(S (NN 'foo') (VP (DET 'a') (VBZ 'bar')))")
    eq_(foo_ts.score(t), 1/3 * 1 * 1 * 1/3)

    t = tree.parse("(S (NN 'bar') (VP (DET 'a') (VBZ 'bar')))")
    eq_(foo_ts.score(t), 1/3 * 1/3 * 1 * 1/3)

    t = tree.parse("(S (NN 'bar') (VP (DET 'every') (VBZ 'foo')))")
    eq_(foo_ts.score(t), 1/3 * 1/3 * 1 * 1/3)
