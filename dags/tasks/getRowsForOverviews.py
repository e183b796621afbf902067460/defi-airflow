from typing import List
from airflow.decorators import task


@task()
def getRowsForOverviews(protocolCategory: str) -> List[tuple]:
    from conf.clients import reader

    query = f'''
        SELECT
            l_addresses_protocols_categories_chains.l_address_protocol_category_chain_id,
            h_addresses.h_address,
            h_protocols.h_protocol_name,
            h_chains.h_network_name
        FROM l_addresses_protocols_categories_chains
        LEFT JOIN l_protocols_categories_chains USING(l_protocol_category_chain_id)
        LEFT JOIN l_protocols_categories USING(l_protocol_category_id)
        LEFT JOIN h_protocols USING(h_protocol_id)
        LEFT JOIN h_protocols_categories USING(h_protocol_category_id)
        LEFT JOIN l_addresses_chains USING(l_address_chain_id)
        LEFT JOIN h_chains ON l_addresses_chains.h_chain_id = h_chains.h_chain_id
        LEFT JOIN h_addresses USING(h_address_id)
        WHERE
            h_protocols_categories.h_protocol_category_name = '{protocolCategory}'
        '''

    return [(row.l_address_protocol_category_chain_id, row.h_address, row.h_protocol_name, row.h_network_name) for row in reader.execute(query=query)]
