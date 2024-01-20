import { Chip, Stack } from "@mui/material";
import { useInstantSearch } from "react-instantsearch";

const SearchHitClips = function (props: {
  county: string;
  locality?: string;
  neighborhood?: string;
  street?: string;
}): JSX.Element {
  const { county, locality, neighborhood, street } = props;
  const { setIndexUiState } = useInstantSearch();

  function refine(
    includeLocality?: boolean,
    includeNeighborhood?: boolean,
    includeStreet?: boolean,
  ) {
    const refinementList: { [attribute: string]: string[] } = {};
    refinementList["county"] = [county];
    if (includeLocality && locality) {
      refinementList["locality"] = [locality];
    }
    if (includeNeighborhood && neighborhood) {
      refinementList["neighborhood"] = [neighborhood];
    }
    if (includeStreet && street) {
      refinementList["street"] = [street];
    }
    setIndexUiState((prevIndexUiState) => ({
      ...prevIndexUiState,
      query: "",
      refinementList: {
        ...prevIndexUiState.refinementList,
        ...refinementList,
      },
    }));
  }

  return (
    <Stack direction="row" spacing={1}>
      {county && (
        <Chip
          label={county}
          size="small"
          className="bg-orange-200"
          onClick={() => refine(false, false, false)}
        />
      )}
      {locality && (
        <Chip
          label={locality}
          size="small"
          className="bg-orange-200"
          onClick={() => refine(true, false, false)}
        />
      )}
      {neighborhood && neighborhood !== locality && (
        <Chip
          label={neighborhood}
          size="small"
          className="bg-orange-200"
          onClick={() => refine(true, true, false)}
        />
      )}
      {street && (
        <Chip
          label={street}
          size="small"
          className="bg-orange-200"
          onClick={() => refine(true, true, true)}
        />
      )}
    </Stack>
  );
};

export default SearchHitClips;
