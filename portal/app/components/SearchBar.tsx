import { Badge, Box, Button, Drawer, Grid, IconButton } from "@mui/material";
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
    <Grid container className="flex w-full">
      <Grid item xs={0} sm={0} md={0} lg={2} />
      <Grid item xs={12} sm={12} md={12} lg={8}>
        <Box className="flex flex-row w-full gap-2 items-center">
          <SearchBox
            className="w-full"
            placeholder="Search property"
            classNames={{
              root: "SearchBox",
              input: "SearchBoxInput",
            }}
          />
          <Badge badgeContent={items.length} color="info" className="font-mono">
            <Button
              variant="outlined"
              onClick={() => openFilters()}
              className="hidden md:block font-mono"
            >
              Filters
            </Button>
            <IconButton
              onClick={() => openFilters()}
              className="block md:hidden"
              aria-label="Open Filters"
            >
              <TuneIcon />
            </IconButton>
          </Badge>
          <Drawer
            anchor="right"
            open={showFilters}
            onClose={() => setShowFilters(false)}
            PaperProps={{ sx: { width: { sm: "100%", md: "30%" } } }}
          >
            <SearchFilters close={closeFilters} clear={clearFilters} />
          </Drawer>
        </Box>
      </Grid>
      <Grid item xs={0} sm={0} md={0} lg={2} />
    </Grid>
  );
};

export default SearchBar;
