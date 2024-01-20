import { Badge, Box, Button, Drawer } from "@mui/material";
import {
  SearchBox,
  useCurrentRefinements,
  useRefinementList,
} from "react-instantsearch";
import "instantsearch.css/themes/satellite.css";
import { useState } from "react";
import SearchFilters from "./SearchFilters";

const SearchBar = function (): JSX.Element {
  const [showFilters, setShowFilters] = useState<boolean>(false);
  useRefinementList({ attribute: "county" });
  useRefinementList({ attribute: "locality" });
  useRefinementList({ attribute: "neighborhood" });
  useRefinementList({ attribute: "street" });
  const { items } = useCurrentRefinements();

  return (
    <Box className="flex flex-row w-full border-b-2 p-5 gap-2">
      <SearchBox className="w-full" placeholder="Search property" />
      <Badge badgeContent={items.length} color="primary">
        <Button onClick={() => setShowFilters(true)}>Filters</Button>
      </Badge>
      <Drawer
        anchor="right"
        open={showFilters}
        onClose={() => setShowFilters(false)}
        PaperProps={{ style: { width: "30%" } }}
      >
        <SearchFilters />
      </Drawer>
    </Box>
  );
};

export default SearchBar;
