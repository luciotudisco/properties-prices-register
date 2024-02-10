/* eslint-disable @typescript-eslint/no-explicit-any */

import { Box, Chip } from "@mui/material";
import { useInstantSearch } from "react-instantsearch";

const SearchHitClips = function (props: { hit: any }): JSX.Element {
  const { hit } = props;
  const { setIndexUiState } = useInstantSearch();

  function refine(
    includeLocality: boolean,
    includeNeighborhood: boolean,
    includeStreet: boolean,
  ) {
    setIndexUiState((prevIndexUiState) => ({
      ...prevIndexUiState,
      query: "",
      refinementList: {
        ...prevIndexUiState.refinementList,
        county: [hit.county],
        locality: includeLocality && hit.locality ? [hit.locality] : [],
        neighborhood:
          includeNeighborhood && hit.neighborhood ? [hit.neighborhood] : [],
        street: includeStreet && hit.street ? [hit.street] : [],
      },
    }));
  }

  return (
    <Box className="w-full flex flex-row flex-wrap gap-2 items-center">
      {hit.county && (
        <Chip
          label={hit.county}
          size="small"
          className="font-thin font-mono"
          onClick={() => refine(false, false, false)}
        />
      )}
      {hit.locality && (
        <Chip
          label={hit.locality}
          size="small"
          className="font-thin font-mono"
          onClick={() => refine(true, false, false)}
        />
      )}
      {hit.neighborhood && hit.neighborhood !== hit.locality && (
        <Chip
          label={hit.neighborhood}
          size="small"
          className="font-thin font-mono"
          onClick={() => refine(true, true, false)}
        />
      )}
      {hit.street && (
        <Chip
          label={hit.street}
          size="small"
          className="font-thin font-mono"
          onClick={() => refine(true, true, true)}
        />
      )}
    </Box>
  );
};

export default SearchHitClips;
