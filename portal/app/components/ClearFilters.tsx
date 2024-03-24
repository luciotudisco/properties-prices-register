import { Button, Flex } from "@mantine/core";
import { useInstantSearch } from "react-instantsearch";

const ClearFilters = function (): JSX.Element {
  const { setIndexUiState } = useInstantSearch();

  function clearFilters() {
    setIndexUiState((prevIndexUiState) => ({
      ...prevIndexUiState,
      query: "",
      refinementList: {},
    }));
  }

  return (
    <Flex align="center" justify="center" className="m-5">
      <Button onClick={clearFilters} variant="light">
        Clear filters
      </Button>
    </Flex>
  );
};

export default ClearFilters;
