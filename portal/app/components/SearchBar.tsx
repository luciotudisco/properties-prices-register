import { Badge, Box, Button, Drawer, Grid } from "@mui/material";
import {
  SearchBox,
  useClearRefinements,
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
  const { refine } = useClearRefinements();

  return (
    <Box className="flex flex-row w-full border-b-2 p-5 gap-2 bg-emerald-950">
      <SearchBox className="w-full" placeholder="Search property" />
      <Badge badgeContent={items.length} color="error">
        <Button onClick={() => setShowFilters(true)} className="text-white">
          Filters
        </Button>
      </Badge>
      <Button onClick={() => refine()} className="text-white">
        Clear
      </Button>
      <Drawer
        anchor="right"
        open={showFilters}
        onClose={() => setShowFilters(false)}
        PaperProps={{ sx: { width: "33%" } }}
      >
        <SearchFilters />
      </Drawer>
    </Box>
  );
};

export default SearchBar;
