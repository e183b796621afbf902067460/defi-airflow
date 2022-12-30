from sqlalchemy import Column, Integer, ForeignKey

from orm.base.main import Base


class SatelliteAddressesProtocolsCategoriesLabelsChains(Base):

    __tablename__ = 's_addresses_protocols_categories_labels_chains'
    __table_args__ = {
        'comment': "Positions in protocol's contracts"
    }

    s_address_protocol_category_label_chain_id = Column(Integer, primary_key=True)
    l_address_protocol_category_chain_id = Column(Integer, ForeignKey('l_addresses_protocols_categories_chains.l_address_protocol_category_chain_id', ondelete='CASCADE'), nullable=False)
