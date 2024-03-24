/* eslint-disable @typescript-eslint/no-explicit-any */

import { Button, Flex } from "@mantine/core";
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
    <Flex
      w="full"
      gap="xs"
      justify="flex-start"
      align="flex-start"
      direction="row"
      wrap="wrap"
    >
      {hit.county && (
        <Button
          variant="light"
          radius="xs"
          size="xs"
          onClick={() => refine(false, false, false)}
        >
          {hit.county}
        </Button>
      )}
      {hit.locality && (
        <Button
          variant="light"
          radius="xs"
          size="xs"
          onClick={() => refine(true, false, false)}
        >
          {hit.locality}
        </Button>
      )}
      {hit.neighborhood && hit.neighborhood !== hit.locality && (
        <Button
          variant="light"
          radius="xs"
          size="xs"
          onClick={() => refine(true, true, false)}
        >
          {hit.neighborhood}
        </Button>
      )}
      {hit.street && (
        <Button
          variant="light"
          radius="xs"
          size="xs"
          onClick={() => refine(true, true, true)}
        >
          {hit.street}
        </Button>
      )}
    </Flex>
  );
};

export default SearchHitClips;
