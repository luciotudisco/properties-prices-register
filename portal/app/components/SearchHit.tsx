/* eslint-disable @typescript-eslint/no-explicit-any */

import { Box, Typography } from "@mui/material";
import { NumericFormat } from "react-number-format";
import Moment from "moment";
import SearchHitClips from "./SearchHitClips";

const SearchHit = function (props: { hit: any }): JSX.Element {
  const { hit } = props;
  return (
    <Box className="w-full h-full p-2 flex flex-row items-center">
      <Box className="flex flex-col w-full h-full gap-2">
        <Typography className="text-gray-900" variant="h5" fontSize="small">
          {hit.raw_address}
        </Typography>
        <Typography className="text-gray-500" variant="h5" fontSize="small">
          {hit.description}
        </Typography>
        <SearchHitClips
          county={hit.county}
          locality={hit.locality}
          neighborhood={hit.neighborhood}
          street={hit.street}
        />
      </Box>
      <Box className="flex flex-col h-full gap-2 items-center justify-center">
        <NumericFormat
          value={hit.price}
          displayType="text"
          thousandSeparator={true}
          className="text-gray-900 text-medium font-bold"
          prefix="€"
        />
        <Typography className="text-gray-500" variant="h5" fontSize="small">
          {Moment(hit.sale_date, "MM/DD/YYYY").format("ll")}
        </Typography>
      </Box>
    </Box>
  );
};

export default SearchHit;
