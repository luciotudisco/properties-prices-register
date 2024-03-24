import { useCurrentRefinements } from "react-instantsearch";
import { Box, Chip, rem } from "@mantine/core";
import { IconX } from "@tabler/icons-react";

const SearchCurrentRefinements = function (): JSX.Element {
  const { items, refine } = useCurrentRefinements();

  return (
    <Box className="flex flex-row flex-wrap gap-2 p-5 justify-center">
      {items.map((item) => (
        <Box className="flex flex-row flex-wrap gap-2">
          {item.refinements.map((refinement) => (
            <Chip
              icon={<IconX style={{ width: rem(16), height: rem(16) }} />}
              defaultChecked={true}
              variant="light"
              onChange={() => refine(refinement)}
            >
              {refinement.label}
            </Chip>
          ))}
        </Box>
      ))}
    </Box>
  );
};

export default SearchCurrentRefinements;
