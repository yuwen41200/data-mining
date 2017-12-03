# Data Mining #

Data Mining Practice

## HW0 Data Preprocessing - Review ##

+ Issues in data preprocessing / data cleaning
  + discard outliers (temperature dataset has unreasonable values like -99.5)
  + ignore, impute or interpolate missing values (taipower dataset lacks data from Jan. to Apr.)
  + align records with n o'clock sharp (make sure there is one and only one record for each hour in both datasets)
+ Flatten JSON to DataFrame: `pandas.io.json.json_normalize()`
+ Write DataFrame to database: `pandas.DataFrame.to_sql()`
+ Calculate Euclidean distance: `numpy.linalg.norm(X - Y)`
+ Other useful functions: `scipy.signal.filtfilt()` for smoothing (noise reduction)
+ Useful programming skills: `f"Hello, my name is {name}."`

## HW1 Association Rules - Review ##

+ Three discretization methods
  + equal width (`pandas.cut()`)
  + equal frequency (`pandas.qcut()`)
  + clustering (e.g. k-means)
+ Investigate DataFrame: `head()`, `describe()`, `corr()`
+ Plot DataFrame
  + `df.A.plot(secondary_y=True, label='name', legend=True)` to add another y-axis
  + `df.A.plot.hist(edgecolor='k')` for histograms
+ We can also discretize multidimensional data.

## HW2 Clustering - Review ##

+ Use elbow method or silhouette value to determine k.
+ For multidimensional data, normalizing data in advance may produce better results.
+ For high-dimensional data, use principal component analysis (PCA) to reduce dimensions.
+ The clustering result of taipower data in `temporal-clustering.ipynb` also shows a periodic pattern.
  + The electricity consumption on weekends tends to belong to a different cluster.
