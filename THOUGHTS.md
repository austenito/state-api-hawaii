I'm not super familiar with the data, so here's just a scratch pad of thoughts
I had concerning each API. I'm going to try to start with the population data.
Once I've completed the first one, the rest should be seamless. **I hope :)**

# Population

Most of the data seems centered around the following attributes:

 * year
 * county
 * population

The data seems to be sliced by various attributes (ie metadata about that
population such as resident vs. non resident, age, sex, etc).  Seems fair that
most of this just be included in the call.  (I'm hoping the various tables are
based off the same sample set - that is, the m/f slice is based off the total
sample size slice.) 

## Endpoints

populations/<year>/<county>

# Other pieces of data

 * prices
 * education
