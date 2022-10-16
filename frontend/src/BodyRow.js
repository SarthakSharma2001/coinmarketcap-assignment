import { SwitchTransition } from 'react-transition-group';
import { Fade, TableCell, TableRow, Box, Avatar } from '@mui/material';
import ArrowDropUpIcon from '@mui/icons-material/ArrowDropUp';
import ArrowDropDownIcon from '@mui/icons-material/ArrowDropDown';
import { numberFormat } from './hooks-helpers';
const BodyRow = ({ row }) => {
  const {
    name,
    one_hour,
    twentyfour_hour,
    seven_day,
    suppy,
    market_cap,
    volume
  } = row;

  const price = numberFormat(row.price, 'currency');

  const renderPercentage = num => {
    return num > 0 ? (
      <Box
        display="flex"
        justifyContent="flex-end"
        alignItems="center"
        color={'success.main'}
      >
        <ArrowDropUpIcon color={'success'} />
        <span>{num}%</span>
      </Box>
    ) : (
      <Box
        display={'flex'}
        justifyContent="flex-end"
        alignItems="center"
        color={'error.main'}
      >
        <ArrowDropDownIcon />
        <span> {num.replace('-', '')}%</span>
      </Box>
    );
  };
  return (
    <TableRow sx={{ '& td': { width: 20 } }}>
      <TableCell
        sx={theme => ({
          [theme.breakpoints.down('md')]: {
            position: 'sticky',
            left: 0,
            zIndex: 10,
            backgroundColor: '#121212',
          },
        })}
      >
        {row.cmc_rank}
      </TableCell>
      <TableCell
        padding="none"
        sx={theme => ({
          [theme.breakpoints.down('md')]: {
            position: 'sticky',
            left: 48,
            zIndex: 10,
            backgroundColor: '#121212',
          },
        })}
      >
        <Box sx={{ display: 'flex', alignItems: 'center' }}>
          <span>
            {name}&nbsp;{row.symbol}
          </span>
        </Box>
      </TableCell>
      <SwitchTransition>
        <Fade key={price}>
          <TableCell align="right">{price}</TableCell>
        </Fade>
      </SwitchTransition>
      <SwitchTransition>
        <Fade key={one_hour}>
          <TableCell align="right">{renderPercentage(one_hour)}</TableCell>
        </Fade>
      </SwitchTransition>
      <SwitchTransition>
        <Fade key={twentyfour_hour}>
          <TableCell align="right">{renderPercentage(twentyfour_hour)}</TableCell>
        </Fade>
      </SwitchTransition>
      <SwitchTransition>
        <Fade key={seven_day}>
          <TableCell align="right">{renderPercentage(seven_day)}</TableCell>
        </Fade>
      </SwitchTransition>
      <TableCell align="right">{market_cap}</TableCell>

      <TableCell align="right">{volume}</TableCell>
      <TableCell align="right">
        {suppy}&nbsp;{row.symbol}
      </TableCell>
    </TableRow>
  );
};

export default BodyRow;
