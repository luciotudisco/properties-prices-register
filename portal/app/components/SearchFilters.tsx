import {
  Badge,
  Box,
  Button,
  Divider,
  IconButton,
  Typography,
} from "@mui/material";
import { useStats } from "react-instantsearch";
import "instantsearch.css/themes/satellite.css";
import SearchFilter from "./SearchFilter";
import CloseIcon from "@mui/icons-material/Close";

const SearchFilters = function (props: {
  close: () => void;
  clear: () => void;
}): JSX.Element {
  const { close, clear } = props;
  const { nbHits } = useStats();

  return (
    <Box className="flex flex-col gap-2 p-2 bg-gray-100">
      <Box className="flex flex-row gap-2 pl-2 pr-2 items-center">
        <Typography
          variant="h6"
          fontWeight="bold"
          fontSize="small"
          textTransform="uppercase"
          className="w-full"
        >
          Filters
        </Typography>
        <IconButton aria-label="close filters" onClick={() => close()}>
          <CloseIcon />
        </IconButton>
      </Box>
      <Divider />
      <Box className="flex flex-col gap-2 pl-5 pr-5">
        <Button
          size="small"
          variant="outlined"
          onClick={() => clear()}
          className="w-full"
        >
          Clear
        </Button>
        <Badge badgeContent={nbHits} color="error" max={99999}>
          <Button
            size="small"
            variant="outlined"
            className="w-full"
            onClick={() => close()}
          >
            Show all
          </Button>
        </Badge>
      </Box>
      <Divider />
      <Box className="flex flex-col gap-5 p-5">
        <SearchFilter attribute="county" />
        <SearchFilter attribute="locality" />
        <SearchFilter attribute="neighborhood" />
        <SearchFilter attribute="street" />
      </Box>
    </Box>
  );
};

export default SearchFilters;
