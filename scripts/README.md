# Scripts

The package includes several useful operational scripts.

## Re-index all properties in Algolia

To re-index all properties in Algolia run the following script:

```shell
make reindex
```

The script retrieve all the properties currently saved in the database using
the ad-hoc list API. Then, it reindexes them in Algolia in batches.
