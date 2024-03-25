import { Button, Flex, Indicator } from "@mantine/core";
import { useInstantSearch, useStats } from "react-instantsearch";

interface FiltersFooterProps {
  opened?: boolean;
  toggle: () => void;
}

const FiltersFooter = function (props: FiltersFooterProps): JSX.Element {
  const { toggle } = props;
  const { setIndexUiState } = useInstantSearch();
  const { nbHits } = useStats();

  function clearFilters() {
    setIndexUiState((prevIndexUiState) => ({
      ...prevIndexUiState,
      query: "",
      refinementList: {},
    }));
    toggle();
  }

  return (
    <Flex align="center" direction="column" className="py-5 px-10" gap="md">
      <Button onClick={clearFilters} variant="light" className="w-full">
        Clear
      </Button>
      <Indicator
        inline
        label={nbHits}
        size={16}
        hiddenFrom="sm"
        className="w-full"
        position="top-end"
      >
        <Button onClick={toggle} variant="light" className="w-full">
          Show
        </Button>
      </Indicator>
    </Flex>
  );
};

export default FiltersFooter;
