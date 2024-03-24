import "instantsearch.css/themes/satellite.css";
import SearchFilter from "./SearchFilter";
import { Flex } from "@mantine/core";

const SearchFilters = function (): JSX.Element {
  return (
    <Flex direction="column" gap="xl" className="m-5">
      <SearchFilter
        attribute="property_type"
        label="property type"
        searchable={false}
        limit={5}
        showMoreLimit={10}
      />
      <SearchFilter
        attribute="county"
        label="county"
        searchable={true}
        limit={5}
        showMoreLimit={10}
      />
      <SearchFilter
        attribute="locality"
        label="locality"
        searchable={true}
        limit={5}
        showMoreLimit={10}
      />
      <SearchFilter
        attribute="neighborhood"
        label="neighborhood"
        searchable={true}
        limit={5}
        showMoreLimit={10}
      />
      <SearchFilter
        attribute="street"
        label="street"
        searchable={true}
        limit={5}
        showMoreLimit={10}
      />
      <SearchFilter
        attribute="sale_year"
        label="sale year"
        searchable={false}
        limit={20}
        showMoreLimit={40}
      />
    </Flex>
  );
};

export default SearchFilters;
