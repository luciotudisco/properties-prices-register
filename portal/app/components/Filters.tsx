import "instantsearch.css/themes/satellite.css";
import Filter from "./Filter";
import { Flex } from "@mantine/core";

const Filters = function (): JSX.Element {
  return (
    <Flex direction="column" gap="xs" m="xs">
      <Filter
        attribute="county"
        label="County"
        searchable={true}
        limit={5}
        showMoreLimit={20}
      />
      <Filter
        attribute="locality"
        label="Locality"
        searchable={true}
        limit={5}
        showMoreLimit={10}
      />
      <Filter
        attribute="neighborhood"
        label="Neighborhood"
        searchable={true}
        limit={5}
        showMoreLimit={10}
      />
      <Filter
        attribute="street"
        label="Street"
        searchable={true}
        limit={5}
        showMoreLimit={10}
      />
      <Filter
        attribute="property_type"
        label="Property Type"
        searchable={false}
        limit={5}
        showMoreLimit={10}
      />
      <Filter
        attribute="sale_year"
        label="Year of sale"
        searchable={false}
        limit={20}
        sortBy="name:desc"
      />
    </Flex>
  );
};

export default Filters;
