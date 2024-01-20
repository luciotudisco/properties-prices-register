import { Box, Typography } from "@mui/material";
import { RefinementList } from "react-instantsearch";
import "instantsearch.css/themes/satellite.css";

const SearchFilter = function (props: {
  attribute: string;
  label: string;
  searchable: boolean;
}): JSX.Element {
  const { attribute, label, searchable } = props;

  return (
    <Box className="flex flex-col gap-2 mt-5">
      <Typography
        className="text-gray-900"
        variant="body1"
        fontSize="small"
        textTransform="uppercase"
        fontWeight="bold"
      >
        {label}
      </Typography>
      <RefinementList
        attribute={attribute}
        limit={5}
        searchable={searchable}
        showMore={true}
      />
    </Box>
  );
};

export default SearchFilter;
