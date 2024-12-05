from Acquisition import aq_inner
from plone.app.contenttypes.browser.collection import CollectionView

from collective.collectiongathering.interfaces import ICollectionGathering


class CollectionGatheringView(CollectionView):
    # def __init__(self, *args, **kwargs):
    #     super(CollectionView, self).__init__(*args, **kwargs)
    #     context = aq_inner(self.context)
    #     # self.collection_behavior = ICollectionGathering(context)
    #     # self.b_size = self.collection_behavior.item_count

    @property
    def collection_behavior(self):
        context = aq_inner(self.context)

        return ICollectionGathering(context)

    @property
    def b_size(self):
        return self.collection_behavior.item_count
