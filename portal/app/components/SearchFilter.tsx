import { Box, Typography } from "@mui/material";
import { RefinementList } from "react-instantsearch";
import "instantsearch.css/themes/satellite.css";

const SearchFilter = function (props: { attribute: string }): JSX.Element {
  const { attribute } = props;

  return (
    <Box className="flex flex-col gap-2 mt-5">
      <Typography
        className="text-gray-900"
        variant="body1"
        fontSize="small"
        textTransform="uppercase"
        fontWeight="bold"
      >
        {attribute}
      </Typography>
      <RefinementList
        attribute={attribute}
        limit={5}
        searchable={true}
        showMore={true}
      />
    </Box>
  );
};

export default SearchFilter;
