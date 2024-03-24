import { useSearchBox } from "react-instantsearch";
import "instantsearch.css/themes/satellite.css";
import { CloseButton, Input } from "@mantine/core";
import { useEffect, useState } from "react";
import { IconSearch } from "@tabler/icons-react";

const SearchBar = function (): JSX.Element {
  const { query, refine } = useSearchBox();
  const [value, setValue] = useState(query);

  useEffect(() => {
    setValue(query);
  }, [query]);

  return (
    <Input
      placeholder="Search property"
      value={value}
      onChange={(event) => {
        refine(event.currentTarget.value);
      }}
      className="md:min-w-96 sm:min-w-72"
      leftSection={<IconSearch size={16} />}
      rightSectionPointerEvents="all"
      rightSection={
        <CloseButton
          aria-label="Clear input"
          onClick={() => refine("")}
          style={{ display: value ? undefined : "none" }}
        />
      }
    />
  );
};

export default SearchBar;
