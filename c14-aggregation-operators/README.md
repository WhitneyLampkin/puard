# C14. Aggregation Operators

> TODO: Add all chapter notes

## Aggregation 

- Aggregation summarizes metrics within one or many applications.
- Agg operators are applied to instant vectors and produce instant vectors.

### Grouping

- `without` - excludes labels from the aggregation
- `by` - only includes specified labels in the aggregation

**Other Grouping Notes**

- Agg operators remove the metric name when the new value changes the meaning of the time series
- Can also provide no labels to `without()`

### Operators

- `sum` - adds up all values in a group
- `count` - counts the number of time series in a group
    - can also count unique values a label has
    - can use multiple counts per expression (inner vs. outer)
- ` avg` - returns avgerage of the values in a group
    - `avg` is the same as `sum()/count()`
- `group` - returns 1 for each time series in a group as a value for the group
    - `sum` and `count` could be used instead but `group` communicates to others that the author was interested in grouping
- `stddev (standard deviation)` - statistical measure of how spread out a set of numbers is
    - **_Used to detect outliers_** - "if one instance in a job has a metric several standard deviations away from the average, that’s a good indication that something is wrong with it."
- `stdvar (standard variance)` - standard deviation squared
- `min` - minimum value within a group
- `max` - maximum value within a group
- `topk` - returns `k`series with the largest value
- `bottomk` - returns `k` series with the smallest value
- `quantile` - returns the specified quantile of the values of the group as the group’s return value.
- `count_values` - builds a frequency histogram of the values of the time series in a group

**Other Operator Notes**

- `topk` and `bottomk` are unique in that:
    1. Labels of time series they return for a gorup are not the labels of the group
    1. Return more than 1 time series per group
    1. Take an additional parameter
- `quantile` also takes an additional parameter
    - Decimal is the quantile percentile