/* eslint-disable @typescript-eslint/no-explicit-any */

import { Grid, Typography } from "@mui/material";
import { NumericFormat } from "react-number-format";
import Moment from "moment";
import SearchHitClips from "./SearchHitClips";

const SearchHit = function (props: { hit: any }): JSX.Element {
  const { hit } = props;
  return (
    <Grid container className="w-full h-full p-2 flex" spacing={2}>
      <Grid item xs={12} md={8} className="flex flex-col w-full h-full gap-2">
        <Typography className="text-gray-900" variant="h5" fontSize="small">
          {hit.raw_address}
        </Typography>
        <Typography className="text-gray-500" variant="h5" fontSize="small">
          {hit.description}
        </Typography>
      </Grid>
      <Grid
        item
        xs={12}
        md={4}
        className="flex flex-col h-full gap-2 md:items-end sm:items-start"
      >
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
      </Grid>
      <Grid item xs={12}>
        <SearchHitClips
          county={hit.county}
          locality={hit.locality}
          neighborhood={hit.neighborhood}
          street={hit.street}
        />
      </Grid>
    </Grid>
  );
};

export default SearchHit;
