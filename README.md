# Plotnine Bunch warning example
This repo contains a minimal example of the matplotlib Bunch deprecation warning triggered by plotnine, mentioned in https://github.com/has2k1/plotnine/issues/205

## Example run
```
$ pipenv run python example.py
/home/chris/.local/share/virtualenvs/plotnine-Bunch-example-K-MQS_cY/lib/python3.6/site-packages/plotnine/coords/coord_cartesian.py:31: MatplotlibDeprecationWarning: The Bunch class was deprecated in Matplotlib 3.0 and will be removed in 3.2. Use types.SimpleNamespace instead.
  self.limits = Bunch(xlim=xlim, ylim=ylim)
/home/chris/.local/share/virtualenvs/plotnine-Bunch-example-K-MQS_cY/lib/python3.6/copy.py:274: MatplotlibDeprecationWarning: The Bunch class was deprecated in Matplotlib 3.0 and will be removed in 3.2. Use types.SimpleNamespace instead.
  y = func(*args)
/home/chris/.local/share/virtualenvs/plotnine-Bunch-example-K-MQS_cY/lib/python3.6/copy.py:274: MatplotlibDeprecationWarning: The Bunch class was deprecated in Matplotlib 3.0 and will be removed in 3.2. Use types.SimpleNamespace instead.
  y = func(*args)
/home/chris/.local/share/virtualenvs/plotnine-Bunch-example-K-MQS_cY/lib/python3.6/site-packages/plotnine/facets/facet.py:151: MatplotlibDeprecationWarning: The Bunch class was deprecated in Matplotlib 3.0 and will be removed in 3.2. Use types.SimpleNamespace instead.
  scales = Bunch()
/home/chris/.local/share/virtualenvs/plotnine-Bunch-example-K-MQS_cY/lib/python3.6/site-packages/plotnine/facets/facet.py:151: MatplotlibDeprecationWarning: The Bunch class was deprecated in Matplotlib 3.0 and will be removed in 3.2. Use types.SimpleNamespace instead.
  scales = Bunch()
/home/chris/.local/share/virtualenvs/plotnine-Bunch-example-K-MQS_cY/lib/python3.6/site-packages/plotnine/facets/layout.py:147: MatplotlibDeprecationWarning: The Bunch class was deprecated in Matplotlib 3.0 and will be removed in 3.2. Use types.SimpleNamespace instead.
  return Bunch(x=xsc, y=ysc)
```
