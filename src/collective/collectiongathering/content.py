from plone.app.contenttypes.interfaces import ICollection
from plone.batching.batch import Batch
from plone.dexterity.content import Container
from zope.interface import implementer

from collective.collectiongathering.interfaces import ICollectionGathering


@implementer(ICollectionGathering)
class CollectionGathering(Container):
    def results(self, batch=True, b_start=0, b_size=None,
                sort_on=None, limit=None, brains=False,
                custom_query=None):
        if not b_size:
            b_size = self.item_count
        if not sort_on:
            sort_on = self.sort_on
        if not limit:
            limit = self.limit

        # Get all results
        collections = [
            collection for collection in self.listFolderContents()
            if ICollection.providedBy(collection)
        ]
        uuids = set()
        results = []
        for collection in collections:
            collection_results = collection.results(
                batch=False, b_start=0, b_size=limit, sort_on=sort_on,
                limit=limit, brains=brains, custom_query=custom_query
            )
            for result in collection_results:
                # Ensure we get each result only once
                if result.uuid() not in uuids:
                    uuids.add(result.uuid())
                    results.append(result)

        # Order the results and limit it
        if sort_on:
            results.sort(key=lambda o: getattr(o, sort_on), reverse=self.sort_reversed)
        if limit:
            results = results[:limit]

        # Batch the results
        results = Batch(results, size=b_size, start=b_start)
        return results
