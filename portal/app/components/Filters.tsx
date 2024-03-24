import "instantsearch.css/themes/satellite.css";
import SearchFilter from "./SearchFilter";
import { Flex } from "@mantine/core";

const Filters = function (): JSX.Element {
  return (
    <Flex direction="column" gap="xs" m="xs">
      <SearchFilter
        attribute="county"
        label="County"
        searchable={true}
        limit={5}
        showMoreLimit={20}
      />
      <SearchFilter
        attribute="locality"
        label="Locality"
        searchable={true}
        limit={5}
        showMoreLimit={10}
      />
      <SearchFilter
        attribute="neighborhood"
        label="Neighborhood"
        searchable={true}
        limit={5}
        showMoreLimit={10}
      />
      <SearchFilter
        attribute="street"
        label="Street"
        searchable={true}
        limit={5}
        showMoreLimit={10}
      />
      <SearchFilter
        attribute="property_type"
        label="Property Type"
        searchable={false}
        limit={5}
        showMoreLimit={10}
      />
      <SearchFilter
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
