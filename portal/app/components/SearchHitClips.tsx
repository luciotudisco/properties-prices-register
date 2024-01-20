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
    includeLocality: boolean,
    includeNeighborhood: boolean,
    includeStreet: boolean,
  ) {
    setIndexUiState((prevIndexUiState) => ({
      ...prevIndexUiState,
      query: "",
      refinementList: {
        ...prevIndexUiState.refinementList,
        county: [county],
        locality: includeLocality && locality ? [locality] : [],
        neighborhood: includeNeighborhood && neighborhood ? [neighborhood] : [],
        street: includeStreet && street ? [street] : [],
      },
    }));
  }

  return (
    <Stack direction="row" spacing={1}>
      {county && (
        <Chip
          label={county}
          size="small"
          className="bg-amber-500"
          onClick={() => refine(false, false, false)}
        />
      )}
      {locality && (
        <Chip
          label={locality}
          size="small"
          className="bg-amber-500"
          onClick={() => refine(true, false, false)}
        />
      )}
      {neighborhood && neighborhood !== locality && (
        <Chip
          label={neighborhood}
          size="small"
          className="bg-amber-500"
          onClick={() => refine(true, true, false)}
        />
      )}
      {street && (
        <Chip
          label={street}
          size="small"
          className="bg-amber-500"
          onClick={() => refine(true, true, true)}
        />
      )}
    </Stack>
  );
};

export default SearchHitClips;
