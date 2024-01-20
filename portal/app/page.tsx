"use client";

import algoliasearch from "algoliasearch";
import Search from "./components/Search";
import { InstantSearch } from "react-instantsearch";
import { Box } from "@mui/material";

const searchClient = algoliasearch(
  "0NVC6NE905",
  "ef099700e7cf4939581005a45ddcdeec",
);

export default function SearchPage() {
  return (
    <Box className="h-full overflow-auto">
      <InstantSearch
        searchClient={searchClient}
        indexName="properties"
        future={{
          preserveSharedStateOnUnmount: true,
        }}
      >
        <Search />
      </InstantSearch>
    </Box>
  );
}
