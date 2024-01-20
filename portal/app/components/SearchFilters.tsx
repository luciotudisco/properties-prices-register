import { Box, Divider } from "@mui/material";
import { ClearRefinements } from "react-instantsearch";
import "instantsearch.css/themes/satellite.css";
import SearchFilter from "./SearchFilter";

const SearchFilters = function (): JSX.Element {
  return (
    <Box className="flex flex-col gap-10 p-5">
      <ClearRefinements />
      <Divider />
      <SearchFilter attribute="county" />
      <SearchFilter attribute="locality" />
      <SearchFilter attribute="neighborhood" />
      <SearchFilter attribute="street" />
    </Box>
  );
};

export default SearchFilters;
