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
    <Box className="flex flex-col gap-2 py-3">
      <Typography
        className="text-gray-900"
        variant="overline"
        fontSize="small"
        textTransform="uppercase"
      >
        {label}
      </Typography>
      <RefinementList
        attribute={attribute}
        limit={5}
        searchable={searchable}
        showMore={true}
        classNames={{
          root: "RefinementList",
          searchBox: "RefinementListSearchBox",
          label: "RefinementListLabel",
          checkbox: "RefinementListCheckbox",
          labelText: "RefinementListLabelText",
          count: "RefinementListCount",
          showMore: "RefinementListShowMore",
        }}
      />
    </Box>
  );
};

export default SearchFilter;
