import { Badge, Box, Button, Drawer, IconButton } from "@mui/material";
import {
  SearchBox,
  useCurrentRefinements,
  useInstantSearch,
  useRefinementList,
} from "react-instantsearch";
import "instantsearch.css/themes/satellite.css";
import { useState } from "react";
import SearchFilters from "./SearchFilters";
import TuneIcon from "@mui/icons-material/Tune";
import ClearIcon from "@mui/icons-material/Clear";

const SearchBar = function (): JSX.Element {
  const [showFilters, setShowFilters] = useState<boolean>(false);
  useRefinementList({ attribute: "property_type" });
  useRefinementList({ attribute: "county" });
  useRefinementList({ attribute: "locality" });
  useRefinementList({ attribute: "neighborhood" });
  useRefinementList({ attribute: "street" });
  useRefinementList({ attribute: "sale_year" });
  const { items } = useCurrentRefinements();
  const { setIndexUiState } = useInstantSearch();

  function clearFilters() {
    setIndexUiState((prevIndexUiState) => ({
      ...prevIndexUiState,
      query: "",
      refinementList: {},
    }));
  }

  function openFilters() {
    setShowFilters(true);
  }

  function closeFilters() {
    setShowFilters(false);
  }

  return (
    <Box className="flex flex-row w-full border-b-2 p-5 gap-2 bg-emerald-950 items-center">
      <SearchBox className="w-full" placeholder="Search property" />
      <Badge badgeContent={items.length} color="error">
        <Button
          onClick={() => openFilters()}
          className="text-white hidden md:block"
        >
          Filters
        </Button>
        <IconButton
          onClick={() => openFilters()}
          className="text-white block md:hidden"
          aria-label="Open Filters"
        >
          <TuneIcon />
        </IconButton>
      </Badge>
      <Button
        onClick={() => clearFilters()}
        className="text-white hidden md:block"
      >
        Clear
      </Button>
      <IconButton
        onClick={() => clearFilters()}
        className="text-white block md:hidden"
        aria-label="Clear Filters"
      >
        <ClearIcon />
      </IconButton>
      <Drawer
        anchor="right"
        open={showFilters}
        onClose={() => setShowFilters(false)}
        PaperProps={{ sx: { width: { sm: "100%", md: "30%" } } }}
      >
        <SearchFilters close={closeFilters} clear={clearFilters} />
      </Drawer>
    </Box>
  );
};

export default SearchBar;
